import subprocess
from . import urgencies

BASE_COMMAND = "notify-send"


def _remove_illegal_chars(text: str):
    output = text.replace('"', '"')
    return output

def _get_urgency(number: int) -> str:
    URGENCIES = {
        1: 'low',
        2: 'normal',
        3: 'critical'
    }
    try:
        return URGENCIES[number]
    except Exception:
        return URGENCIES[2]

def notify(
    title: str,
    description: str,
    urgency: int = None,
    icon: str = None,
    timeout: str = None,
):
    if not urgency:
        urgency = urgencies.NORMAL
    _urgency = _get_urgency(urgency)
    title = _remove_illegal_chars(title)
    description = _remove_illegal_chars(description)
    COMMAND = f'{BASE_COMMAND} "{title}" "{description}" -u {_urgency} '
    if icon:
        COMMAND += f"-i {icon} "
    if timeout:
        COMMAND += f"-t {timeout} "
    return subprocess.call(COMMAND, shell=True)
