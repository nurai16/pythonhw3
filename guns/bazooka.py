class Bazooka:
    has_grenade = True

    def shoot(self):
        print('Kaboom')
        self.has_grenade = False

    def reload(self):
        print('Reloading...')
        self.has_grenade = True

    def grenade_exists(self):
        if self.has_grenade:
            print('Ready to blow something')
        else:
            print('Need to reload...')


