context = """
                 You are an assistant to generate a bootstrab code of an example of table of relevant informations about vehicule and  a big DFMEA table, bordered-table for the vehicle part in the given review, just the code with random data,real component and sub-components in the given review, anything else, do not say anything, no comments, no cdns, juste the bootstrap code ... In the code do not add any comments
Do not include theses tags or elements :
Head
Script
Style
Link
Comments (like <!-- Repeat the above <tr> structure as needed for each row --> ) 

the only balise you are allowed to generate is the table balise, anything else."""

content = """we bought this 99 cherokee inline 6 back in 2004 with 70,000 miles. over the years the biggest repair that was needed was the rear main seal replacement at 280,000 miles. other than that it has been the usual replacement of parts that will eventually wear out with time. the engine has never been stripped down to do an overhaul or replace anything, besides spark plugs and the like. now at 305,000 miles the engine still sounds the same from when we bought it. the mpg reads 15 but i tested this and found that it is getting 21 in the city. awesome. oil change every 3000 miles and other regular maintenance and i believe this engine will go to 400,000 without an overhaul. people complain about the ride being crappy which is correct, but then you don't buy a jeep for comfort. this vehicle is a true utility truck. and it actually handles quite well in the city. jeep designed a great truck with the cherokee and plan on keeping this going for as long as i can. eventually will restore this back to factory look and feel."""

response = """
  <h3 class="text text-center"> Relevant informations </h3>
<table class="table table-bordered">
 <thead>
  <tr>
   <th>
    Description
   </th>
   <th>
    Value
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    Year of Purchase
   </td>
   <td>
    2004
   </td>
  </tr>
  <tr>
   <td>
    Mileage at Purchase
   </td>
   <td>
    70,000 miles
   </td>
  </tr>
  <tr>
   <td>
    Major Repairs
   </td>
   <td>
    Rear main seal replacement at 280,000 miles
   </td>
  </tr>
  <tr>
   <td>
    Regular Maintenance
   </td>
   <td>
    Oil change every 3,000 miles, spark plug replacement, etc.
   </td>
  </tr>
  <tr>
   <td>
    Current Mileage
   </td>
   <td>
    305,000 miles
   </td>
  </tr>
  <tr>
   <td>
    Current MPG
   </td>
   <td>
    15
   </td>
  </tr>
  <tr>
   <td>
    Actual MPG (City)
   </td>
   <td>
    21
   </td>
  </tr>
  <tr>
   <td>
    Comfort Level
   </td>
   <td>
    Crappy (as expected for a utility truck)
   </td>
  </tr>
  <tr>
   <td>
    Handling
   </td>
   <td>
    Quite well in the city
   </td>
  </tr>
  <tr>
   <td>
    Future Plans
   </td>
   <td>
    Restore back to factory look and feel
   </td>
  </tr>
 </tbody>
</table>


<h3 class="text text-center"> DFMEA TABLE </h3>
<table class="table table-bordered">
  <thead>
    <tr>
      <th>Component</th>
      <th>Potential Failure Modes</th>
      <th>Potential Effects</th>
      <th>Potential Causes</th>
      <th>Current Controls</th>
      <th>Severity (S)</th>
      <th>Occurrence (O)</th>
      <th>Detection (D)</th>
      <th>Risk Priority Number (RPN)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Engine</td>
      <td>Wear, Overheating, Seizure</td>
      <td>Reduced Power, Engine Damage</td>
      <td>Lack of Maintenance, High Mileage</td>
      <td>Regular maintenance, Diagnostic tests</td>
      <td>7</td>
      <td>6</td>
      <td>7</td>
      <td>294</td>
    </tr>
    <tr>
      <td>Rear Main Seal</td>
      <td>Oil Leak, Seal Cracking</td>
      <td>Oil Loss, Engine Damage</td>
      <td>Normal Wear and Tear, Poor Installation</td>
      <td>Inspection, Replacement</td>
      <td>7</td>
      <td>2</td>
      <td>8</td>
      <td>112</td>
    </tr>
    <tr>
      <td>Spark Plugs</td>
      <td>Fouling, Erosion, Misfire</td>
      <td>Poor Fuel Efficiency, Engine Misfires</td>
      <td>Normal Wear and Tear, Poor Fuel Quality</td>
      <td>Regular maintenance, Inspection</td>
      <td>4</td>
      <td>4</td>
      <td>6</td>
      <td>96</td>
    </tr>
    <tr>
      <td>Ride Quality</td>
      <td>Suspension Failure, Shocks Wear</td>
      <td>Uncomfortable Ride, Reduced Handling</td>
      <td>Normal Wear and Tear, Poor Road Conditions</td>
      <td>Regular maintenance, Inspection</td>
      <td>4</td>
      <td>5</td>
      <td>9</td>
      <td>180</td>
    </tr>
    <tr>
      <td>Utility Truck Design</td>
      <td>Lack of Comfort Features</td>
      <td>Uncomfortable Ride, Reduced Comfort</td>
      <td>Design Choice, Lack of Features</td>
      <td>N/A</td>
      <td>4</td>
      <td>2</td>
      <td>4</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
"""

example = [
    {
        "role": "user",
        "content": content,
    }, {
        "role": "assistant",
        "content": response,
    }]
