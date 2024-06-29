import re
from datetime import datetime
from zoneinfo import ZoneInfo

readme = 'README.md'
this_tz = ZoneInfo("Asia/Shanghai")
start_comment = '<!--START_SECTION:progress-->'
end_comment = '<!--END_SECTION:progress-->'
placeholder = fr'{start_comment}[\s\S]+{end_comment}'


def gen_progress_content() -> str:
    progress_bar_capacity = 50
    current_time_of_this_year = datetime.timestamp(datetime.now())
    this_year = datetime.now().year
    start_time_of_this_year = datetime.timestamp(
        datetime(datetime.now().year, 1, 1, 0, 0, 0, 0, this_tz))
    end_time_of_this_year = datetime.timestamp(
        datetime(datetime.now().year, 12, 31, 23, 59, 59, 0, this_tz))
    progress_of_this_year = ((current_time_of_this_year - start_time_of_this_year)
                             / (end_time_of_this_year - start_time_of_this_year))
    progress_bar = (f'{int(progress_bar_capacity * progress_of_this_year) * "⣿"}'
                    f'{"" if progress_of_this_year == 1 else "⣦"}'
                    f'{int(progress_bar_capacity - 1 - progress_bar_capacity * progress_of_this_year) * "⣀"}')
    progress_content = f"""{start_comment}
⌛ Progress of {this_year}

{progress_bar} {100 * progress_of_this_year:.2f}%
{end_comment}"""
    return progress_content


def gen_readme() -> None:
    progress_content = gen_progress_content()
    with open(readme, 'r') as r:
        readme_content = r.read()
    with open(readme, 'w') as w:
        n_readme_content = re.sub(placeholder, progress_content, readme_content)
        print(n_readme_content)
        w.write(n_readme_content)


if __name__ == '__main__':
    gen_readme()
