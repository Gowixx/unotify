import unotify

## Icons List
## > https://specifications.freedesktop.org/icon-naming-spec/latest/ar01s04.html

unotify.notify(
    title = 'Testing',
    description = 'uNotify example.',
    urgency = unotify.urgencies.NORMAL,
    timeout = 10,
    icon = 'edit-undo'
)