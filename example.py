import unotify

## Icons List
## > https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html

unotify.notify(
    title = 'Testing',
    message = 'uNotify example.',
    urgency = unotify.urgencies.NORMAL,
    timeout = 10,
    app_name = 'Testing',
    app_icon = 'edit-undo'
)
