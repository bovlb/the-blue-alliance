#Documentation - The Blue Alliance API
The Blue Alliance is a [FIRST Robotics](http://www.usfirst.org/) match archive website. The Blue Alliance API provides you with the same data available on The Blue Alliance website. This data includes team information, event information and match results.

##API Clients
TODO: Put info when someone writes a client

##Usage
The API returns data in JSON format. For more information on JSON, visit [json.org](http://www.json.org/). There you will also find links to JSON libraries for many programming languages.

###Teams

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
          <td>key,team_number,name,nickname,website,event_keys,location</td>
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
          <td>key,team_number,name,nickname,website,event_keys,location,locality,country,region</td>
     </tr>
     <tr>
          <td>Example</td>
          <td><a href="http://www.thebluealliance.com/api/v1/team/details?team=frc281">http://www.thebluealliance.com/api/v1/team/details?team=frc281</a></td>
     </tr>
</table>

###Events

####ApiEventsShow

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