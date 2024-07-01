import re
import uuid
from datetime import datetime
from zoneinfo import ZoneInfo

readme = 'README.md'
this_tz = ZoneInfo("Asia/Shanghai")
start_comment = '<!--START_SECTION:progress-->'
end_comment = '<!--END_SECTION:progress-->'
placeholder = fr'{start_comment}[\s\S]+{end_comment}'
progress_bar_capacity = 50


def gen_progress_content(capacity: int, tz: ZoneInfo) -> str:
    seed = uuid.uuid1()
    current_time_of_this_year = datetime.timestamp(datetime.now())
    this_year = datetime.now().year
    start_time_of_this_year = datetime.timestamp(
        datetime(this_year, 1, 1, 0, 0, 0, 0, tz))
    end_time_of_this_year = datetime.timestamp(
        datetime(this_year, 12, 31, 23, 59, 59, 0, tz))
    progress_of_this_year = ((current_time_of_this_year - start_time_of_this_year)
                             / (end_time_of_this_year - start_time_of_this_year))
    progress_bar = (f'{int(capacity * progress_of_this_year) * "⣿"}'
                    f'{"" if progress_of_this_year == 1 else "⣦"}'
                    f'{int(capacity - 1 - capacity * progress_of_this_year) * "⣀"}')
    progress_content = f"""{start_comment}
⌛ Progress of {this_year}
<!--{seed}-->
{progress_bar} {100 * progress_of_this_year:.2f}%
{end_comment}"""
    return progress_content


def gen_readme() -> None:
    progress_content = gen_progress_content(progress_bar_capacity, this_tz)
    with open(readme, 'r') as r:
        readme_content = r.read()
    with open(readme, 'w') as w:
        n_readme_content = re.sub(placeholder, progress_content, readme_content)
        print(n_readme_content)
        w.write(n_readme_content)


if __name__ == '__main__':
    gen_readme()
