# DAY-50 (100 Days of Code Python)

## Auto Tinder Swiping Bot

* Important Links: 
  * [This Person Does Not Exist](https://www.thispersondoesnotexist.com)      <!-- You can hit refresh on thispersondoesnotexist to generate new random images. -->

[>](https://github.com/Aniruddh-482/Python/blob/main/Auto%20Tinder%20Swiping%20Bot/main.py) Step 1 - Setup your account on Tinder <br>

[>](https://github.com/Aniruddh-482/Python/blob/main/Auto%20Tinder%20Swiping%20Bot/main.py) Step 2 - Navigate to Login Page <br>

[>](https://github.com/Aniruddh-482/Python/blob/main/Auto%20Tinder%20Swiping%20Bot/main.py) Step 3 - Login with Facebook <br>
<!--
In Selenium, each window has a identification handle, we can get all the window handles with:

    driver.window_handles

The above line of code returns a list of all the window handles. The first window is at position 0 e.g.

    base_window = driver.window_handles[0]

New windows that have popped out from the base_window are further down in the sequence e.g.

    fb_login_window = driver.window_handles[1]

We can switch our Selenium to target the new facebook login window by:

    driver.switch_to.window(fb_login_window)

You can print the driver.title to verify that it's the facebook login window that is currently target:

    print(driver.title)

The full code to switch to the new pop-up window is thus:

    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)

If successful the printed title should be "Facebook" and not "Tinder | Match. Chat. Date." 
-->
<!--
NOTE: Avoid invoking the Facebook Login too frequently, see if you can test your code without logging in, 
you don't want to appear like a bot to Facebook as there is always the chance that they might disable your FB account. 
Alternatively, you can try setting up an alternative Facebook account.
-->

[>](https://github.com/Aniruddh-482/Python/blob/main/Auto%20Tinder%20Swiping%20Bot/main.py) Step 4 - Dismiss all requests <br>

[>](https://github.com/Aniruddh-482/Python/blob/main/Auto%20Tinder%20Swiping%20Bot/main.py) Step 5 - Hit Like! <br>
<hr>

