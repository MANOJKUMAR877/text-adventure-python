import world
from player import Player
import sound
def play():
    space = 1
    sound.Space()
    while space <=2:
        world.load_tiles('map.txt')
        player = Player()
        if space ==2:
            world.load_tiles('map2.txt')
            player = Player()
        room = world.tile_exists(player.location_x, player.location_y)
        print(room.intro_text())
        while player.is_alive() and not player.victory:

           room = world.tile_exists(player.location_x, player.location_y)
           room.modify_player(player)
        # Check again since the room could have changed the player's state
           if player.is_alive() and not player.victory:

                print("Hey Astronaut choose the move:\n")
                available_actions = room.available_actions()
                for action in available_actions:
                    print(action)
                    action_input = input('Your Jump: ')
                    for action in available_actions:
                       if action_input == action.hotkey:
                          player.do_action(action, **action.kwargs)
                          break
        if player.is_alive() and player.victory:
            space =+1
            continue

if __name__ == "__main__":
    play()