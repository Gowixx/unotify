import unotify
from unotify import urgencies
## Icons List
## > https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html

unotify.notify(
    title="Testing",
    message="uNotify example.",
    urgency=urgencies.NORMAL,
    timeout=10,
    app_name="Testing",
    app_icon="edit-undo"
)
