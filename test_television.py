
from television import Television


def test_init():
    # Create a new television object
    tv = Television()

    # Check the default television values
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_power():
    # Create a new television object
    tv = Television()

    # Turn the television on
    tv.power()

    # Check that the television is on
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Turn the television off
    tv.power()

    # Check that the television is off
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_mute():
    # Create a new television object
    tv = Television()

    # Turn the television on
    tv.power()

    # Increase the volume
    tv.volume_up()

    # Check the volume before muting
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # Mute the television
    tv.mute()

    # Check that the volume displays zero
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Unmute the television
    tv.mute()

    # Check that the original volume returns
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_channel_up():
    # Create a new television object
    tv = Television()

    # Check that the channel does not change when off
    tv.channel_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # Turn the television on
    tv.power()

    # Increase the channel
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'

    # Increase to the maximum channel
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'

    # Check that the channel returns to the minimum
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

def test_channel_down():
    # Create a new television object
    tv = Television()

    # Check that the channel does not change when off
    tv.channel_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # Turn the television on
    tv.power()

    # Decrease the channel from the minimum
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'

    # Decrease the channel
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 2, Volume = 0'

    # Decrease to the minimum channel
    tv.channel_down()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Check that the channel returns to the maximum
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'

def test_volume_up():
    # Create a new television object
    tv = Television()

    # Check that the volume does not change when off
    tv.volume_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # Turn the television on
    tv.power()

    # Increase the volume
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # Increase to the maximum volume
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

    # Check that the volume does not exceed the maximum
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

    # Mute the television
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Increase the volume to unmute
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

def test_volume_down():
    # Create a new television object
    tv = Television()

    # Check that the volume does not change when off
    tv.volume_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # Turn the television on
    tv.power()

    # Increase the volume to the maximum
    tv.volume_up()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

    # Decrease the volume
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    # Decrease to the minimum volume
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Check that the volume does not go below the minimum
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Increase the volume and mute the television
    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    # Decrease the volume to unmute
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

def test_str():
    # Create a new television object
    tv = Television()

    # Check the default television information
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    # Turn on the television
    tv.power()

    # Change the channel and volume
    tv.channel_up()
    tv.volume_up()

    # Check the updated television information
    assert str(tv) == 'Power = True, Channel = 1, Volume = 1'

    # Mute the television
    tv.mute()

    # Check that the displayed volume is zero
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'
