# Treatment Preferences Questionnaire Variables

The interviewer will read the statements below to the participant first. We are interested in the type of opioid use disorder treatment the participant would most prefer if all options were available to the participant now. The questions below ask in more detail about the participants most preferred treatment type. (Please note: the treatment types below are not necessarily offered in this study).


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Variable Name</th>
      <th>Description</th>
      <th>Possible Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M1</td>
      <td>If respondent is not a candidate for OUD treatment, mark here and skip this set of items.</td>
      <td>N/A not a candidate for OUD treatment</td>
    </tr>
    <tr>
      <td>M2</td>
      <td>Which type of opioid use disorder (OUD) treatment would you most prefer to receive if it were available to you now? (CHECK ALL THAT APPLY): [1] OUD medication (e.g. methadone, buprenorphine/Suboxone, naltrexone/Vivitrol) [Ask M3], [2] Detox, [3] Outpatient counseling, [4] Residential treatment, [5] Other (specify): _______________, [6] No treatment, [7] Don’t know / No preference. [SKIP LOGIC:  If M2=1, ask M3, otherwise go to next set of questions]</td>
      <td>array</td>
    </tr>
    <tr>
      <td>M3</td>
      <td>Which OUD medication treatment type would you most prefer to receive if it were available to you now? (SELECT ONLY ONE): [1] Methadone, [2] Buprenorphine/Suboxone (ASK M4), [3] Naltrexone/Vivitrol (ASK M5), [4] Don’t Know / No Preference. [SKIP LOGIC:  If M3=2, ask M4. If M3=3, ask M5. Otherwise go to next set of questions.]</td>
      <td>1<br>2<br>3<br>4</td>
    </tr>
    <tr>
      <td>M4</td>
      <td>Which type of buprenorphine? [SELECT ONLY ONE and go to next set of questions]: [1] I would prefer to receive daily buprenorphine-naloxone sublingual tablets or films (Suboxone®), [2] I would prefer to receive monthly or weekly buprenorphine injections (e.g., Sublocade®, Brixadi®), [3] I would prefer to receive the 6-month buprenorphine implant (Probuphine®), [4] Don’t Know / No Preference.</td>
      <td>1<br>2<br>3<br>4</td>
    </tr>
    <tr>
      <td>M5</td>
      <td>Which type of naltrexone?  (SELECT ONLY ONE): [1] I would prefer to receive daily buprenorphine-naloxone sublingual tablets or films (Suboxone®), [2] I would prefer to receive monthly or weekly buprenorphine injections (e.g., Sublocade®, Brixadi®), [3] I would prefer to receive the 6-month buprenorphine implant (Probuphine®), [4] Don’t Know / No Preference.</td>
      <td>1<br>2<br>3<br>4</td>
    </tr>
    <tr>
      <td>comments</td>
      <td>Additional comments that need to be captured.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>created_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>follow_ups.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>follow_ups.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>project_id</td>
      <td>Unique ID for any specific defined piece of work that is undertaken or attempted to meet a single requirement.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>state</td>
      <td>The current state of the object.</td>
      <td>uploading<br>uploaded<br>md5summing<br>md5summed<br>validating<br>error<br>invalid<br>suppressed<br>redacted<br>live<br>validated<br>submitted<br>released</td>
    </tr>
    <tr>
      <td>submitter_id</td>
      <td>A project-specific identifier for a node. This property is the calling card/nickname/alias for a unit of submission. It can be used in place of the UUID for identifying or recalling a node.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>type</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>updated_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
  </tbody>
</table>