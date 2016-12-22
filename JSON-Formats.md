## For Event Webcasts

List of dicts where each dict is as follows:

**Livestream:** `{"type": "livestream", "channel": "<channel id #>", "file": "<event id #>"}`
* Example: `{"type": "livestream", "channel": "3136927", "file": "1964881"}`

**Justin TV:** `{"type": "justin", "channel": "<channel name>"}`
* Example: `{"type": "justin", "channel": "frc604"}`

**Twitch TV:** `{"type": "twitch", "channel": "<channel name>"}`
* Example: `{"type": "twitch", "channel": "tbacast"}`

**Ustream:** `{"type": "ustream", "channel": "<channel id #>"}`
* Example: `{"type": "ustream", "channel": "6540154"}`

**RTMP:** `{"type": "rtmp", "channel": "<stream URL>", "file": "<file name>"}`
* Example: `{"type": "rtmp", "channel": "cp76072.live.edgefcs.net/live/", "file": "MED-HQ-Flash@42814"}`

## For Special Webcasts
The `gameday.special_webcasts` sitevar contains information about extra webcasts as well as other metadata for GameDay.
**Example:** 
```json
{
  "webcasts": [
    {
      "key_name": "firstupdatesnow",
      "type": "twitch",
      "name": "FIRST Updates Now",
      "channel": "firstupdatesnow"
    },
    {
      "key_name": "gamesense",
      "type": "twitch",
      "name": "GameSense",
      "channel": "frcgamesense"
    }
  ],
  "aliases": {
    "fun": "#layout=0&view_0=firstupdatesnow-1",
    "gamesense": "#layout=0&view_0=frcgamesense-1"
  }
}
```