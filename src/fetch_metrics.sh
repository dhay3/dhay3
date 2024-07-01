#!/usr/bin/env bash

set -xo

# https://github.com/vn7n24fzkq/github-profile-summary-cards
declare -r PROFILE_SUMMARY_CARDS_DARK_URL="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=dhay3&theme=2077"
declare -r PROFILE_SUMMARY_CARDS_URL="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=dhay3&theme=github"

# https://github.com/anuraghazra/github-readme-stats
declare -r README_STATS_DARK_URL="https://github-readme-stats.vercel.app/api?username=dhay3&show_icons=true&theme=radical&hide_title=true&card_width=500&hide_border=true"
declare -r README_STATS_URL="https://github-readme-stats.vercel.app/api?username=dhay3&show_icons=true&theme=transparent&hide_title=true&card_width=500&hide_border=true"

# https://github.com/JacobLinCool/LeetCode-Stats-Card
declare -r LEET_CARD_DARK_URL="https://leetcard.jacoblin.cool/dhay3?site=cn&theme=dark"
declare -r LEET_CARD_URL="https://leetcard.jacoblin.cool/dhay3?site=cn&theme=light"

wget -O assets/profile_summary_card_dark.svg ${PROFILE_SUMMARY_CARDS_DARK_URL} \
&& wget -O assets/profile_summary_card.svg ${PROFILE_SUMMARY_CARDS_URL} \
&& sed -i -e 's/width="700"/width="500"/' \
-e 's/height="200"/height="165"/' \
-e 's/dhay3 (CyperPelican)//' \
-e 's/stroke="#e4e2e2"//' \
-e 's/stroke="#141321"//' \
assets/profile_summary_card_dark.svg assets/profile_summary_card.svg

wget -O assets/readme_card_dark.svg ${README_STATS_DARK_URL} \
&& wget -O assets/readme_card.svg ${README_STATS_URL}

wget -O assets/leet_card_dark.svg ${LEET_CARD_DARK_URL} \
&& wget -O assets/leet_card.svg ${LEET_CARD_URL} \
&& sed -i -e 's/stroke:var(--bg-2);//g' \
assets/leet_card_dark.svg assets/leet_card.svg