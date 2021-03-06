import random
from constants import *
from game.casting.animation import Animation
from game.casting.santa import Santa
from game.casting.body import Body
from game.casting.gift import Gift
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.boy import Boy
from game.casting.stats import Stats
from game.casting.text import Text 
from game.casting.background import Background
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_gift_action import CollideGiftAction
from game.scripting.collide_boy_action import CollideBoyAction
from game.scripting.control_boy_action import ControlBoyAction
from game.scripting.draw_background_action import DrawBackgroundAction
from game.scripting.draw_santa_action import DrawSantaAction
from game.scripting.draw_gifts_action import DrawGiftsAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_boy_action import DrawBoyAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_santa_action import MoveSantaAction
from game.scripting.move_boy_action import MoveBoyAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.move_gifts_action import MoveGiftsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_GIFTS_ACTION = CollideGiftAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BOY_ACTION = CollideBoyAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_BOY_ACTION = ControlBoyAction(KEYBOARD_SERVICE)
    DRAW_BACKGROUND_ACTION = DrawBackgroundAction(VIDEO_SERVICE)
    DRAW_SANTA_ACTION = DrawSantaAction(VIDEO_SERVICE)
    DRAW_GIFTS_ACTION = DrawGiftsAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_BOY_ACTION= DrawBoyAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_SANTA_ACTION = MoveSantaAction()
    MOVE_BOY_ACTION = MoveBoyAction()
    MOVE_GIFTS_ACTION = MoveGiftsAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == INSTRUCTIONS:    
            self._prepare_instructions(cast, script)
        elif scene == LEVEL:
            self._prepare_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
        elif scene == PAUSE:    
            self._prepare_pause(cast, script)    

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

# Menu screen
    def _prepare_new_game(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        # text with logo and instructions to start
        self._add_dialog(cast, GAME_NAME, FONT_FILE_LOGO, FONT_SIZE_LOGO, ALIGN_CENTER, Point(CENTER_X, 0))
        self._add_dialog(cast, ENTER_TO_START, FONT_FILE, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, CENTER_Y), True)
        self._add_dialog(cast, H_TO_INSTRUCTIONS, FONT_FILE, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 100), True)
        self._add_dialog(cast, P_TO_PAUSE, FONT_FILE, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, CENTER_Y + 200), True)

        self._add_background(cast, MENU_IMAGE)

        # actions to move to other scenes
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, LEVEL, ENTER))
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, INSTRUCTIONS, HELP))

        output_elements = [
            self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION, 
        ]

        self._add_initialize_script(script)
        self._add_load_script(script)
        self._add_output_script(script, output_elements)
        self._add_unload_script(script)
        self._add_release_script(script)

# Instructions screen
    def _prepare_instructions(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        # text with instructions on how to play the game
        self._add_dialog(cast, RED_GIFT_INSTRUCTIONS, FONT_FILE, FONT_SMALL, ALIGN_LEFT, Point(25, 100), True)
        self._add_dialog(cast, GREEN_GIFT_INSTRUCTIONS, FONT_FILE, FONT_SMALL, ALIGN_LEFT, Point(25, 200), True)
        self._add_dialog(cast, COAL_INSTRUCTIONS, FONT_FILE, FONT_SMALL, ALIGN_LEFT, Point(25, 300), True)
        self._add_dialog(cast, OVER_INSTRUCTIONS, FONT_FILE, FONT_SMALL, ALIGN_LEFT, Point(25, 400), True)

        # how to go to menu
        self._add_dialog(cast, M_TO_MENU, FONT_FILE, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, 500), True)
        
        self._add_background(cast, MENU_IMAGE)

        # actions to move to other scenes
        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEW_GAME, MENU))

        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, output_elements)

# prepare game to start
    def _prepare_level(self, cast, script):
        # add actors to game
        self._add_stats(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_santa(cast)
        self._add_gifts(cast)
        self._add_boy(cast)
        self._add_background(cast, BACKGROUND_IMAGE)
        self._add_dialog(cast, PREP_TO_LAUNCH, FONT_FILE, FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y))

        # actions to move to other scenes
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        
        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_SANTA_ACTION,
            self.DRAW_GIFTS_ACTION,
            self.DRAW_BOY_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, output_elements)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))

# Scene when game is over        
    def _prepare_try_again(self, cast, script):
        self._add_dialog(cast, WAS_GOOD_GAME, FONT_FILE, FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y))
        
        # clear actions to stop all sprites from moving
        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)

        # wait 3 seconds and move to final scene
        script.add_action(INPUT, TimedChangeSceneAction(GAME_OVER, 3))
        
        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_SANTA_ACTION,
            self.DRAW_GIFTS_ACTION,
            self.DRAW_BOY_ACTION,
            self.DRAW_DIALOG_ACTION
        ]
        self._add_output_script(script, output_elements)

# while playing action
    def _prepare_in_play(self, cast, script):
        # clear texts from MENU
        cast.clear_actors(DIALOG_GROUP)

        # actions to move to other scenes
        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_BOY_ACTION)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, LEVEL, RESTART))
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEW_GAME, MENU))
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, PAUSE, PAUSE_P))
        self._add_update_script(script)

        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_SANTA_ACTION,
            self.DRAW_GIFTS_ACTION,
            self.DRAW_BOY_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, output_elements)

# Pause the game
    def _prepare_pause(self, cast, script):
        # Stop movement and all actions
        script.clear_actions(INPUT)
        script.clear_actions(UPDATE)
        script.clear_actions(OUTPUT)

        # Add 'Pause' text
        self._add_dialog(cast, PAUSE_TEXT, FONT_FILE, FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, CENTER_Y))
        
        # Recursive function to Pause the game 
        script.add_action(INPUT, TimedChangeSceneAction(PAUSE, 30))
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, IN_PLAY, PAUSE_P))

        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_HUD_ACTION,
            self.DRAW_SANTA_ACTION,
            self.DRAW_GIFTS_ACTION,
            self.DRAW_BOY_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, output_elements)

# Final scene
    def _prepare_game_over(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)

        # display final score
        stats = cast.get_first_actor(STATS_GROUP)
        
        self._add_dialog(cast, WAS_GOOD_GAME, FONT_FILE_LOGO, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, CENTER_Y))
        self._add_dialog(cast, FINAL_SCORE + str(stats.get_score()), FONT_FILE, FONT_LARGE, ALIGN_CENTER, Point(CENTER_X, 100), True)
        self._add_dialog(cast, M_TO_MENU, FONT_FILE, FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, 450), True)
        self._add_dialog(cast, R_TO_RESTART, FONT_FILE, FONT_SMALL, ALIGN_CENTER, Point(CENTER_X, 550), True)
        self._add_background(cast, GAME_OVER_IMAGE)

        # actions to move to other scenes
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, LEVEL, RESTART))
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEW_GAME, MENU))
        script.clear_actions(UPDATE)

        output_elements = [self.DRAW_BACKGROUND_ACTION,
            self.DRAW_DIALOG_ACTION
        ]

        self._add_output_script(script, output_elements)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    def _add_background(self, cast, image_path):
        cast.clear_actors(BACKGROUND_GROUP)
        x = (0)
        y = (0)
        position = Point(x, y)
        size = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
        body = Body(position, size)
        image = Image(image_path)
        background = Background(body, image, True)
        cast.add_actor(BACKGROUND_GROUP, background)

    def _add_santa(self, cast):
        cast.clear_actors(SANTA_GROUP)
        x = (0)
        y = (10)
        position = Point(x, y)
        size = Point(SANTA_WIDTH, SANTA_HEIGHT)
        velocity = Point(3, 0)
        body = Body(position, size, velocity)
        image = Image(SANTA_IMAGE)
        santa = Santa(body, image, True)
        cast.add_actor(SANTA_GROUP, santa)

    def _add_gifts(self, cast):
        cast.clear_actors(GIFT_GROUP)
        
        for i in range(GIFT_QUANTITY):
            x = random.randrange(FIELD_LEFT, FIELD_RIGHT - GIFT_WIDTH)
            y = Y_DISTANCE * (i+1)
            position = Point(x, y)
            
            size = Point(GIFT_WIDTH, GIFT_HEIGHT)
            
            vel_x = random.randrange(-2, 2)
            vel_y = 3
            velocity = Point(vel_x, vel_y)

            type_of_gift = random.randrange(0,3)
            body = Body(position, size, velocity)
            gift = Gift(body, type_of_gift, True)

            cast.add_actor(GIFT_GROUP, gift)

    def _add_dialog(self, cast, message, file, size, alignment, p_position, multiple=False):
        if multiple == False:
            cast.clear_actors(DIALOG_GROUP)
        label = Label(Text(message, file, size, alignment), p_position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_boy(self, cast):
        cast.clear_actors(BOY_GROUP)
        x = CENTER_X - BOY_WIDTH / 2
        y = SCREEN_HEIGHT - 200
        position = Point(x, y)
        size = Point(BOY_WIDTH, BOY_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BOY_IMAGE)
        boy = Boy(body, image, True)
        cast.add_actor(BOY_GROUP, boy)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script, list):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)

        for i in list:
            script.add_action(OUTPUT, i)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_SANTA_ACTION)
        script.add_action(UPDATE, self.MOVE_GIFTS_ACTION)
        script.add_action(UPDATE, self.MOVE_BOY_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_GIFTS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BOY_ACTION)
        script.add_action(UPDATE, self.MOVE_BOY_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)