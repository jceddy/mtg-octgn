changelog = {
    3020300: ("3.2.3.0", "07 October 2013", [
        "Added a changelog dialog that displays when a game is started.",
        "Added a table submenu to separately enable/disable alignment, autoscripts, and attachment aligning.",
        "Attaching a card to another player's card will pass control of it to your opponent.",
        "Detached auras will trigger destroy scripts remotely for the player who controls the aura.",
        "Manually moving a card around the table will move all its attachments with it (while attachment aligning is enabled).",
        "Fixed the mana symbols showing up in the chat log.",
        "Added Theros Intro packs and Event deck.",
        "RTR's Izzet Ingenuity intro deck now contains the correct basic lands.",
        "Fixed Clear All (esc) not removing target arrows.",
        "Clear All (esc) will not remove the Does Not Untap highlight.",
        "Removed all manipulations of cards you don't control from alignment code (all done remotely now)."
        ]),
    3020400: ("3.2.4.0", "09 October 2013", [
        "Fixed a game-breaking bug involving the attachments script.",
        "Initial support for Monstrosity abilities.",
        "Added marker images for Monstrous, Morph and Choice autoscript indicators.",
        "Fixed activated model abilities asking to choose an ability twice.",
        "Fixed a bug where casting an aura with a target would align the aura behind the target, instead of on the stack."
        ]),
    3020500: ("3.2.5.0", "23 October 2013", [
        "Added 'Scry' Library action (CTRL+SHIFT+C), which lets you scry a specified number of cards on top of your library.",
        "Added a catch to prevent a few illegal attachment pairings.",
        "Bestow creatures will now auto-attach like auras if you target something while casting them.",
        "Behind the scenes changes to askChoice dialog windows, and the Stack alignment."
        ]),
    3020600: ("3.2.6.0", "30 October 2013", [
        "Added Commander 2013 cards and decks."
        ]),
    3020700: ("3.2.7.0", "11 December 2013", [
        "Alignment no longer breaks when a player leaves the game.",
        "Cards entering the battlefield won't zoom out the tale.",
        "Fixed a python error when you cancel out of the scry window.",
        "Fixed ampersands showing up in the mana costs of some cards."
        ]),
    3020800: ("3.2.8.0", "12 December 2013", [
        "Fixed a bug where this changelog window kept popping up.",
        "Favorite Token artworks will now be saved properly.",
        "Attack, block, exile, activate, tap/untap process faster when performed on a selection of cards.",
        "Fixed some bugs with the alignment and autoscript toggles."
        ]),
    3020900: ("3.2.9.0", "17 December 2013", [
        "Added Theros Prerelease Packs to the sealed deck editor.",
        "Added a debug option in the 'Autoscript Settings' menu. It will be used to debug lag times in the game.",
        "Manually moving a card on the table will anchor it to the table, blocking it from alignment.",
        "Added 'Align Card' action for cards on the table.  Using this on an anchored card will remove the anchor and align the card.",
        "Using the 'Re-Align Cards' table action now removes the anchors on all cards, forcing them to align."
        ]),
    3021000: ("3.2.10.0", "20 January  2014", [
        "Added an Autoscript Setting to toggle Alignment Anchoring.",
        "-> Enabled: Manually dragging a card will anchor it.  Card alignment will ignore it.",
        "-> Disabled: Manually dragging a card will allow you to rearrange the order of your cards with alignment.",
        "Added more data to the debug option.",
        "Added 'Pass Priority' (F6) toggle function which will automatically pass your priority if you have Autoscripts enabled.",
        "Added some missing tokens from the Commander sets.",
        "Fixed Xenagos's Token and the corruped 10th Edition intro decks."
        ]),
    3021100: ("3.2.11.0", "28 January 2014", [
        "Added Born of the Gods cards and tokens.",
        "Updated the Help document for some newer functions.",
        "Added 'View Update Log' action for the table, to view all previous changelog windows."
        ]),
    3021200: ("3.2.12.0", "05 May 2014", [
        "Added Duel Decks Jace vs Vraska cards & Preconstructed Decks.",
        "Added Journey into Nyx cards, Tokens, Preconstructed Decks.",
        "Added Born of the Gods and Journey Into Nyx Prerelease Seeded Booster Packs."
        ]),
    3021202: ("3.2.12.2", "22 May 2014", [
        "Quick Matchmaking update, multiple formats are now available for matchmaking."
        ]),
    3021300: ("3.2.13.0", "06 June 2014", [
        "Added Conspiracy+tokens, and Modern Event Deck 2014."
        ]),
    3021400: ("3.2.14.0", "08 July 2014", [
        "Added M15+Tokens, and Vintage Masters.",
        "Added M15 Clash Pack deck files, found in the Event Decks folder"
        ]),
    3021501: ("3.2.15.1", "16 September 2014", [
        "Added Khans of Tarkir+Tokens.",
        "Updated the card database for the most recent Oracle text.",
        "Added the Challenge Decks and Hero supplemental cards from Theros Block.",
        "Updated the pre-con decks (Khans decks not yet available).",
        "Fixed a bug where peeked Morph cards (facedown) will align with their face-up equivalents, revealing the card identity to other players.",
        "Updated script recognition of the new Modal card template.",
        "Casting a card face-down (Morphing it) will auto-peek it for you."
        ]),
    3021600: ("3.2.16.0", "18 September 2014", [
        "Updated Khans of Tarkir to the Gatherer text.",
        "Khans and Ravnica watermarks now show on proxy images.",
        "Added Speed vs Cunning and FTV Annihilation.",
        "Fixed a bug stopping morph triggers from triggering."
        ]),
    3021602: ("3.2.16.2", "05 November 2014", [
        "Added Commander 2014 set and tokens."
        ]),
    3021700: ("3.2.17.0", "13 January 2015", [
        "Added Fate Reforged cards and tokens.",
        "Added Khans of Tarkir Seeded Boosters (You'll need to add both the Booster and the Promo pack to generate a complete Seeded booster pack.)",
        "Fixed a bug preventing Planeswalkers and other cards activated abilities from working."
        ])
}