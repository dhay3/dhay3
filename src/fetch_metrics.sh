#!/usr/bin/env bash

declare -r LEETCODE_METRICS_URL="https://leetcard.jacoblin.cool/dhay3?site=cn&theme=dark"
declare -r PROFILE_SUMMARY_URL="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=dhay3&theme=2077"
declare -r README_STAT_URL="https://github-readme-stats.vercel.app/api?username=dhay3&show_icons=true&theme=radical&hide_title=true&card_width=500&hide_border=true"

wget ${LEETCODE_METRICS_URL}