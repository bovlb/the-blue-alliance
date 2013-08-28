#Documentation - The Blue Alliance API
The Blue Alliance is a [FIRST Robotics](http://www.usfirst.org/) match archive website. The Blue Alliance API provides you with the same data available on The Blue Alliance website. This data includes team information, event information and match results.

##Usage
The API returns data in JSON format. For more information on JSON, visit [json.org](http://www.json.org/). There you will also find links to JSON libraries for many programming languages.

##Teams

####ApiTeamsShow

<table>
     <tr>
          <td>Description</td>
          <td>Information about teams</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/teams/show</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>teams</em>, a <a href="http://en.wikipedia.org/wiki/Comma-separated_values">CSV</a> string of team_keys</td>
     </tr>
     <tr>
          <td>Returns</td>
          <td>List of teams. Each team contains its key_name, team_number, name, nickname, website, event_keys, location</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/teams/show?teams=frc281,frc1114">http://www.thebluealliance.com/api/v1/teams/show?teams=frc281,frc1114</a></td>
     </tr>
</table>

####ApiTeamsDetails

<table>
     <tr>
          <td>Description</td>
          <td>Detailed information about a particular team</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/team/details</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>team</em>, a team_key of the format "frc####"</td>
     </tr>
     <tr>
          <td>Returns</td>
          <td>key_name, team_number, name, nickname, website, event_keys, location, locality, country, region</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/team/details?team=frc281">http://www.thebluealliance.com/api/v1/team/details?team=frc281</a></td>
     </tr>
</table>

##Events

<a name="ApiEventList"></a>
####ApiEventList

<table>
     <tr>
          <td>Description</td>
          <td>List of events for a particular year</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/events/list</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>year</em>, a string of the format YYYY</td>
     </tr>
     <tr>
          <td>Returns</td>
          <td>A list of events. Each event contains its key_name, name, short_name, whether its an official event or not, and start_date/end_date in ISO format if available.</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/events/list?year=2012">http://www.thebluealliance.com/api/v1/events/list?year=2012</a></td>
     </tr>
</table>

<a name="ApiEventDetails"></a>
####ApiEventDetails

<table>
     <tr>
          <td>Description</td>
          <td>Get all details for a particular event</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/events/details</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>event</em>, an event key</td>
     </tr>
     <tr>
          <td>Returns</td>
          <td>For the event specified: key_name, year, event_code, name, short_name, location, whether its an official event or not, facebook_eid, start_date, end_date, list of teams, list of matches.</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/event/details?event=2012ct">http://www.thebluealliance.com/api/v1/event/details?event=2012ct</a></td>
     </tr>
</table>

####ApiMatchDetails

<table>
     <tr>
          <td>Description</td>
          <td>Information about matches</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/match/show</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>match[es]</em>, a string of the match key. Also accepts a CSV string of keys .</td>
     </tr>
     <tr>
          <td></td>
          <td><em>events</em>, a <a href="http://en.wikipedia.org/wiki/Comma-separated_values">CSV</a> string of event_keys</td> 
     </tr>
     <tr>
          <td>Returns</td>
          <td>key_name, event, competition_level, set_number, match_number, team_keys, alliances</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/match/details?match=2010cmp_f1m1">http://www.thebluealliance.com/api/v1/match/details?match=2010cmp_f1m1</a></td>
     </tr>
</table>

##Deprecated

####ApiEventsShow

> Warning: ApiEventsShow has been deprecated. It may not be available in future versions of the API. Please consider using [ApiEventList](#ApiEventList) and [ApiEventDetails](#ApiEventDetails) instead.

<table>
     <tr>
          <td>Description</td>
          <td>Information about events</td>
     </tr>
     <tr>
          <td>URL</td>
          <td>/api/v1/events/show</td>
     </tr>
     <tr>
          <td>Accepts</td>
          <td><em>year</em>, a string of the format YYYY</td>
     </tr>
     <tr>
          <td></td>
          <td><em>events</em>, a <a href="http://en.wikipedia.org/wiki/Comma-separated_values">CSV</a> string of event_keys</td> 
     </tr>
     <tr>
          <td>Returns</td>
          <td>???</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/events/show?events=2012ct">http://www.thebluealliance.com/api/v1/events/show?events=2012ct</a></td>
     </tr>
</table>