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
          <td>http://www.thebluealliance.com/api/v1/teams/show?teams=frc281,frc1114</td>
     </tr>
</table>