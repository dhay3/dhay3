import re
import logging
from datetime import datetime

current_time_of_this_year = datetime.timestamp(datetime.now())
this_year = datetime.now().year
this_time_zone = datetime.now().astimezone().tzinfo
start_time_of_this_year = datetime.timestamp(
    datetime(datetime.now().year, 1, 1, 0, 0, 0, 0, this_time_zone))
end_time_of_this_year = datetime.timestamp(
    datetime(datetime.now().year, 12, 31, 23, 59, 59, 0, this_time_zone))
progress_of_this_year = ((current_time_of_this_year - start_time_of_this_year) /
                         (end_time_of_this_year - start_time_of_this_year))


def gen_progress_bar() -> str:
    progress_bar_capacity = 50
    return (f'{int(progress_bar_capacity * progress_of_this_year) * "⣿"}'
            '⣦'
            f'{int(progress_bar_capacity - 1 - progress_bar_capacity * progress_of_this_year) * "⣀"}')


def gen_readme() -> None:
    start_comment = '<!--START_SECTION:progress-->'
    end_comment = '<!--END_SECTION:progress-->'
    placeholder = fr'{start_comment}[\s\S]+{end_comment}'
    progress_bar = gen_progress_bar()
    progress_content = f"""{start_comment}
⌛ Progress of {this_year}
{progress_bar} {100 * progress_of_this_year:.2f}%
{end_comment}
"""
    with open('README.md', 'r') as r:
        readme_content = r.read()
    with open('README.txt', 'w') as w:
        w.write(re.sub(placeholder, progress_content, readme_content))


if __name__ == '__main__':
    gen_readme()
    with open('README.md', 'r') as f:
        print(f.read())
