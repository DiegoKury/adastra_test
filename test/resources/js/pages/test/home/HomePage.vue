<template>
  <div class="home-page">
    <h1 class="display-5 fw-bold text-center">Zones and Distributions</h1>

    <template>
      <div class="col-lg-6 mx-auto zones mb">
        <zone-editable
          v-for="zone in zones"
          :id="zone.id"
          :name="zone.name"
          :distributions="zone.distributions"
          :updated_at="zone.updated_at"
          :key="zone.uid"
          :zoneNames="zoneNames"
          @edit="editZone"
          class="zone"
        />
      </div>
    </template>

    <h1 class="display-5 fw-bold text-center">To Do List</h1>

    <ul class="col-lg-6 mx-auto">
      <li>
        DONE - Add the percentage symbol to each distribution number while is
        not being edited
      </li>
      <li>DONE - The cancel button is not working</li>
      <li>
        DONE - Without refreshing the page, be able to edit all the
        distributions from a zone
      </li>
      <li>DONE - Be able to add more distributions</li>
      <li>DONE - Be able to remove distributions</li>
      <li>
        DONE - When the user is not able to save due to some error, the error
        must be showed
      </li>
      <li>
        DONE - The sum of all distributions must be ensured to be 100% in anyway
      </li>
      <li>DONE - The distributions must be integer</li>
      <li>DONE - The zone name cannot be empty</li>
      <li>
        DONE - The zone name cannot have more than one space between each word
      </li>
      <li>DONE - The zone name cannot have spaces at start or the end</li>
      <li>DONE - The zone name cannot be repeated in any way</li>
      <li>
        DONE - Create a new field "updated_at" that is going to store the date
        when the name field change
      </li>
      <li>DONE - Show the updated_at field value near each zone name</li>
      <li>
        DONE - Add a way for the user to know that an element is being saved
      </li>
      <li>
        DONE - When the number of distributions is 5 or greater, the background
        of that zone must change to any color while is not being edited
      </li>
      <li>DONE - Make it so elements are saved even after reload</li>
    </ul>
  </div>
</template>

<script>
import ZoneEditable from "./ZoneEditable.vue";

export default {
  name: "HomePage",
  components: {
    ZoneEditable,
  },
  props: {
    context: {
      type: Object,
    },
  },
  data() {
    return {
      zones: [],
      zoneUid: 0,
    };
  },
  // Added to check for repeated names
  computed: {
    zoneNames() {
      return this.zones.map((zone) => zone.name);
    },
  },
  mounted() {
    this.zones = this.context.zones.map((data) => {
      return {
        id: data.id,
        name: data.name,
        uid: this.zoneUid++,
        distributions: data.distributions,
        updated_at: data.updated_at,
      };
    });
  },
  methods: {
    editZone(updatedZone) {
      const apiUrl = "http://localhost:8000/api/put";

      // Prepare the request data
      const requestData = {
        id: updatedZone.id,
        name: updatedZone.name,
        distributions: updatedZone.distributions,
        updated_at: updatedZone.updated_at,
      };

      // Send the PUT request to the API
      fetch(apiUrl, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(requestData),
      })
        .then((response) => {
          if (response.ok) {
            // Zone edited successfully
            console.log("Zone edited successfully");
          } else {
            // Failed to edit zone
            console.error("Failed to edit zone");
          }
        })
        .catch((error) => {
          // An error occurred while editing zone
          console.error("An error occurred while editing zone:", error);
        });

      // Update the zone locally
      const zone = this.zones.find((z) => z.id === updatedZone.id);
      if (zone) {
        zone.name = updatedZone.name;
        zone.distributions = updatedZone.distributions;
        zone.updated_at = updatedZone.updated_at;
      }
    },
  },
};
</script>

<style lang="scss">
@import "resources/scss/variables.scss";

.home-page {
  .zones {
    display: flex;
    gap: 4px;
    flex-direction: column;
  }
}
</style>
