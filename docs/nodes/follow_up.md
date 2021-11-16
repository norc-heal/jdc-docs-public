# Follow Up Variables

A visit by a patient or study participant to a medical professional. A clinical encounter that encompasses planned and unplanned trial interventions, procedures and assessments that may be performed on a subject. A visit has a start and an end, each described with a rule. The process by which information about the health status of an individual is obtained before and after a study has officially closed; an activity that continues something that has already begun or that repeats something that has already been done.


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
      <td>Baseline_participant_characteristics_using_GAIN_Q3</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>Re_arrest_within_6_months_using_admin_data</td>
      <td>TBD</td>
      <td>boolean</td>
    </tr>
    <tr>
      <td>admin_data_to_get_count_of_arrests</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>admin_data_to_get_count_of_incarceration_days</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>admin_data_to_get_count_of_incarceration_episodes</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>admission_and_release_dates_from_jail_using_admin_data</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>age_at_visit</td>
      <td>Age at visit in years - round to nearest integer. If the age in years at the visit is greater than 89, see 'age_at_visit_gt89'.</td>
      <td>integer<br>null</td>
    </tr>
    <tr>
      <td>age_at_visit_gt89</td>
      <td>Indicate if the age at visit years is greater than 89.</td>
      <td>Yes<br>No</td>
    </tr>
    <tr>
      <td>bmi</td>
      <td>The body mass divided by the square of the body height expressed in units of kg/m^2.</td>
      <td>number</td>
    </tr>
    <tr>
      <td>completed_follow_up</td>
      <td>TBD</td>
      <td>boolean</td>
    </tr>
    <tr>
      <td>completed_terms_of_mandates_using_admin_data</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>completed_treatment</td>
      <td>blank</td>
      <td>string</td>
    </tr>
    <tr>
      <td>created_datetime</td>
      <td>A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]</td>
      <td>string<br>null</td>
    </tr>
    <tr>
      <td>days_to_follow_up</td>
      <td>Number of days between the date used for index and the date the patient was seen or contacted at follow-up.</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>drug_used</td>
      <td>Ever used any medical or recreational drugs since last visit</td>
      <td>No<br>Yes<br>Refusal<br>Unknown</td>
    </tr>
    <tr>
      <td>education_level</td>
      <td>An indication of the years of schooling completed in graded public, private, or parochial schools, and in colleges, universities, or professional schools.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>ever_transferred</td>
      <td>Participant ever transferred sites (changed ids)</td>
      <td>Never transferred<br>Transferred</td>
    </tr>
    <tr>
      <td>food_insecurity</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>health_insurance</td>
      <td>Currently have any health insurance</td>
      <td>boolean</td>
    </tr>
    <tr>
      <td>height</td>
      <td>The height of the patient in centimeters.</td>
      <td>number<br>null</td>
    </tr>
    <tr>
      <td>housing_status</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>locator_information</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
    <tr>
      <td>marital_status</td>
      <td>A demographic parameter indicating a person's current conjugal status.</td>
      <td>single<br>married<br>divorced<br>widowed</td>
    </tr>
    <tr>
      <td>participants.id</td>
      <td>A 128-bit identifier. Depending on the mechanism used to generate it, it is either guaranteed to be different from all other UUIDs/GUIDs generated until 3400 AD or extremely likely to be different. Its relatively small size lends itself well to sorting, ordering, and hashing of all sorts, storing in databases, simple allocation, and ease of programming in general.</td>
      <td>string</td>
    </tr>
    <tr>
      <td>participants.submitter_id</td>
      <td>No description</td>
      <td>string</td>
    </tr>
    <tr>
      <td>pregnancy_status</td>
      <td>Is the participant pregnant (women) or has been pregnant since the last visit</td>
      <td>boolean</td>
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
      <td>termination_reason</td>
      <td>blank</td>
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
    <tr>
      <td>version_data</td>
      <td>Version number of data</td>
      <td>string</td>
    </tr>
    <tr>
      <td>visit_date</td>
      <td>Year of the visit.</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>visit_id</td>
      <td>ID at time of interview (prior to transfer)</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>visit_name</td>
      <td>Visit ID (string)</td>
      <td>string</td>
    </tr>
    <tr>
      <td>visit_number</td>
      <td>Visit number</td>
      <td>integer</td>
    </tr>
    <tr>
      <td>visit_type</td>
      <td>Define if the visit is a follow-up or the baseline visit.</td>
      <td>Baseline Visit<br>Follow-up Visit<br>Abbreviated Visit (Record in ABRV file)</td>
    </tr>
    <tr>
      <td>weight</td>
      <td>The weight of the subject measured in grams.</td>
      <td>number</td>
    </tr>
    <tr>
      <td>weight_percentage</td>
      <td>The percentage of the weight considering the weight measured at the index date as the reference.</td>
      <td>number</td>
    </tr>
    <tr>
      <td>zip_code</td>
      <td>TBD</td>
      <td>string</td>
    </tr>
  </tbody>
</table>