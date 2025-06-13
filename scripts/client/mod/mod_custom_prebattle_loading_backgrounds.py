import ResMgr, random
from gui.Scaleform.Prebattle import Prebattle

def get_random_mod_bg(leaf_folder):
    res_path = 'gui/flash'
    base_path = 'imagePrebattleLoading'
    relative_path = '%s/%s' % (base_path, leaf_folder)
    full_path = '%s/%s' % (res_path, relative_path)

    section = ResMgr.openSection(full_path, False)
    if section is None:
        print 'Can\'t find path ' + full_path
        return None

    extensions = ('.dds', '.jpg', '.png')
    images = [n for n in section.keys() if n.lower().endswith(extensions)]
    if not images:
        print 'no imagines found in ' + full_path
        return None

    choice = random.choice(images)
    return '%s/%s' % (relative_path, choice)

_orig_ctor = Prebattle.__init__
def _patched_ctor(self, *args, **kwargs):
    _orig_ctor(self, *args, **kwargs)
    self.addExternalCallbacks({'python.getRandomModBg': get_random_mod_bg})

Prebattle.__init__ = _patched_ctor