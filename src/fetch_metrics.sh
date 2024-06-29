#!/usr/bin/env bash

declare -r PROFILE_SUMMARY_CARDS_URL="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=dhay3&theme=2077"
declare -r README_STATS_URL="https://github-readme-stats.vercel.app/api?username=dhay3&show_icons=true&theme=radical&hide_title=true&card_width=500&hide_border=true"
declare -r LEET_CARD_URL="https://leetcard.jacoblin.cool/dhay3?site=cn&theme=dark"

wget -O assets/profile_summary_card.svg ${PROFILE_SUMMARY_CARDS_URL}
wget -O assets/readme_card.svg ${README_STATS_URL}
wget -O assets/leet_card.svg ${LEET_CARD_URL}