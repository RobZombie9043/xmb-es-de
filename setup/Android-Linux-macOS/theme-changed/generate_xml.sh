#!/usr/bin/env sh

# Determine the script's base directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(dirname "$(dirname "$SCRIPT_DIR")")"  # Goes up from /scripts/theme-changed

# Only run if new theme is 'xmb-es-de'
if [ "$1" != "xmb-es-de-main" ]; then
    echo "⏩ Skipping script: new theme is not xmb-es-de (got '$1')"
    exit 0
fi

LOG_PATH="$BASE_DIR/logs/es_log.txt"
OUTPUT_DIR="$BASE_DIR/themes/xmb-es-de-main/theme-customizations/gamelist-carousel"

mkdir -p "$OUTPUT_DIR"

if [ ! -r "$LOG_PATH" ]; then
    echo "❌ Failed to read log file at $LOG_PATH"
    exit 1
fi

TMP_NAMES="$OUTPUT_DIR/tmp_names.txt"
TMP_ORDERED="$OUTPUT_DIR/tmp_ordered.txt"

# Check for individual custom collection entries
HAS_INDIVIDUAL_CUSTOM_COLLECTIONS=false
if grep -q 'for custom collection "' "$LOG_PATH"; then
    HAS_INDIVIDUAL_CUSTOM_COLLECTIONS=true
fi

# Extract names from log
grep 'Populating gamelist for' "$LOG_PATH" | while read -r line; do
    case "$line" in
        *'for system "'*)
            name=$(echo "$line" | sed -n 's/.*for system "\([^"]*\)".*/\1/p')
            case "$name" in
                all) mapped_name="auto-allgames" ;;
                favorites) mapped_name="auto-favorites" ;;
                recent) mapped_name="auto-lastplayed" ;;
                collections) mapped_name="custom-collections" ;;
                *) mapped_name="$name" ;;
            esac
            echo "$mapped_name"
            ;;
        *'for custom collection "'*)
            name=$(echo "$line" | sed -n 's/.*for custom collection "\([^"]*\)".*/\1/p')
            echo "$name"
            ;;
    esac
done > "$TMP_NAMES"

# Remove duplicates, keep first occurrence
awk '!seen[$0]++' "$TMP_NAMES" > "$TMP_ORDERED"

TOTAL=$(wc -l < "$TMP_ORDERED" | tr -d ' ')

# Function to get line with wrapping (1-based indexing)
get_name_at() {
    idx=$1
    while [ "$idx" -le 0 ]; do idx=$((idx + TOTAL)); done
    while [ "$idx" -gt "$TOTAL" ]; do idx=$((idx - TOTAL)); done
    sed -n "${idx}p" "$TMP_ORDERED"
}

i=1
while [ $i -le $TOTAL ]; do
    current=$(get_name_at "$i")

    m2=$(get_name_at $((i - 2)))
    m1=$(get_name_at $((i - 1)))
    p1=$(get_name_at $((i + 1)))
    p2=$(get_name_at $((i + 2)))
    p3=$(get_name_at $((i + 3)))
    p4=$(get_name_at $((i + 4)))
    p5=$(get_name_at $((i + 5)))
    p6=$(get_name_at $((i + 6)))
    p7=$(get_name_at $((i + 7)))

    # Determine output file
    if echo "$current" | grep -q '^custom-'; then
        if [ "$HAS_INDIVIDUAL_CUSTOM_COLLECTIONS" = true ]; then
            xmlfile="$OUTPUT_DIR/${current}.xml"
        else
            xmlfile="$OUTPUT_DIR/custom-collections.xml"
        fi
    elif [ "$current" = "collections" ]; then
        if [ "$HAS_INDIVIDUAL_CUSTOM_COLLECTIONS" = true ]; then
            echo "Skipping 'collections' system because individual custom collections are present"
            i=$((i + 1))
            continue
        else
            xmlfile="$OUTPUT_DIR/collections.xml"
        fi
    else
        xmlfile="$OUTPUT_DIR/${current}.xml"
    fi

    echo "Writing XML file: $xmlfile"

    {
        echo '<?xml version="1.0" ?>'
        echo '<theme>'
        echo '    <variables>'
        echo "        <systemMinus2>$m2</systemMinus2>"
        echo "        <systemMinus1>$m1</systemMinus1>"
        echo "        <systemPlus1>$p1</systemPlus1>"
        echo "        <systemPlus2>$p2</systemPlus2>"
        echo "        <systemPlus3>$p3</systemPlus3>"
        echo "        <systemPlus4>$p4</systemPlus4>"
        echo "        <systemPlus5>$p5</systemPlus5>"
        echo "        <systemPlus6>$p6</systemPlus6>"
        echo "        <systemPlus7>$p7</systemPlus7>"
        echo '    </variables>'
        echo '</theme>'
    } > "$xmlfile"

    if [ -f "$xmlfile" ]; then
        echo "✅ Created $xmlfile"
    else
        echo "❌ Failed to create $xmlfile"
    fi

    i=$((i + 1))
done

# Clean up
rm -f "$TMP_NAMES" "$TMP_ORDERED"
