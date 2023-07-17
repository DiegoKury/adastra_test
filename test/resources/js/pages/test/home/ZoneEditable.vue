<template>
  <div
    class="zone-editable"
    :class="{ 'zone-editable--gray': hasManyDistributions && display }"
  >
    <div v-if="display" class="zone-display">
      <!-- Display mode -->
      <div>
        Zone Name: <strong>{{ name }}</strong> Distributions:
        {{ distributionDisplay }}
      </div>
      <!-- Updated-at text -->
      <div v-if="updated_at !== ''" class="zone-updated-at">
        <span class="zone-updated-at-text">Updated At:</span>
        <span class="zone-updated-at-value">{{ updated_at }}</span>
      </div>
      <button
        class="btn btn-primary"
        @click="setDisplay(false)"
        :disabled="saving"
      >
        Edit
      </button>
    </div>
    <div v-else class="zone-edit">
      <!-- Edit mode -->
      <label class="control-label"> Zone Name </label>

      <input
        v-model="form.name"
        placeholder="Zone name"
        class="form-control"
        :disabled="saving"
        @input="validateName"
      />

      <!-- Error message -->
      <div v-if="error !== ''" class="error-message">{{ error }}</div>

      <div class="zone-edit-distributions">
        <div v-for="(distribution, index) in form.distributions" :key="index">
          <div class="distribution-item">
            <!-- Delete distribution button -->
            <button
              class="btn btn-danger btn-sm"
              @click="deleteDistribution(index)"
            >
              -
            </button>

            <!-- Distribution input -->
            <label class="control-label"> Distribution </label>
            <input
              v-model="distribution.percentage"
              placeholder="Percentage"
              class="form-control"
            />
          </div>
        </div>

        <!-- Add distribution button -->
        <button
          class="btn btn-secondary"
          @click="addDistribution"
          :disabled="saving"
        >
          Add Distribution
        </button>
      </div>

      <div class="zone-edit-actions">
        <!-- Cancel and Save buttons -->
        <button class="btn btn-secondary" :disabled="saving" @click="cancel">
          Cancel
        </button>

        <button class="btn btn-success" @click="save" :disabled="saving">
          <span v-if="saving">Saving...</span>
          <span v-else>Save</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ZoneEditable",
  props: {
    name: String,
    id: Number,
    distributions: Array,
    zoneNames: Array, // Added to check for repeated names
    updated_at: String, // Added updated_at variable
  },
  data() {
    return {
      display: true,
      form: {
        name: "",
        distributions: [],
      },
      saving: false,
      error: "", // Added error variable
    };
  },
  /* Added a '%' to the right of the percentage value.
  Also added some space around the hyphen. */
  computed: {
    distributionDisplay() {
      return this.distributions
        .map((distribution) => distribution.percentage + "%")
        .join(" - ");
    },
    // Checks if there are more than 5 distributions
    hasManyDistributions() {
      return this.form.distributions.length >= 5;
    },
  },
  mounted() {
    this.getValuesFromProps();
  },
  methods: {
    getValuesFromProps() {
      this.form.distributions = this.distributions.map((distribution) => {
        return {
          id: distribution.id,
          percentage: distribution.percentage,
          error: "", // Added error property for each distribution
        };
      });
    },
    setDisplay(value) {
      this.display = value;

      if (!this.display) {
        this.getValuesFromProps();
      }
    },

    // New method for adding distributions
    addDistribution() {
      this.form.distributions.push({
        id: null,
        percentage: "",
        error: "", // Added error property for each new distribution
      });
    },
    // New method for deleting distributions
    deleteDistribution(index) {
      this.form.distributions.splice(index, 1);
    },
    
    // Modified save method
    async save() {

      // Error check 1: Validate the zone name does not have more than one space between each word
      if (/\s{2,}/.test(this.form.name)) {
        this.error =
          "The zone name cannot have more than one space between each word";
          return;
      }

      // Error check 2: Validate the zone name is not empty
      if (!this.form.name.trim()) {
        this.error = "The zone name cannot be empty";
        return;
      }

      // Error check 3: Validate the zone name is not repeated
      const isNameRepeated = this.zoneNames.some((name) => {
        return (
          name.trim() === this.form.name.trim() &&
          name.trim() !== this.name.trim()
        );
      });
      if (isNameRepeated) {
        this.error = "The zone name cannot be repeated";
        return;
      }

      // Error check 4: Validate the zone name does not have spaces at the start or end
      if (this.form.name.trim() !== this.form.name) {
        this.error = "The zone name cannot have spaces at the start or the end";
        return;
      }

      // Error check 5: Validate that all distribution percentages are valid numbers
      const hasInvalidPercentage = this.form.distributions.some(
        (distribution) => {
          const percentage = String(distribution.percentage).trim();
          return (
            !/^\d+(\.\d+)?$/.test(percentage) || parseFloat(percentage) === 0
          );
        },
      );
      if (hasInvalidPercentage) {
        this.error =
          "Distribution percentage must be a valid number greater than 0";
        return;
      }

      // Error check 6: Validate the distributions are integers
      let hasError = false;
      this.form.distributions.forEach((distribution, index) => {
        if (!Number.isInteger(parseFloat(distribution.percentage))) {
          this.error = "The distribution must be an integer";
          hasError = true;
          return;
        }
      });
      if (hasError) {
        return;
      }

      // Error check 7: Validate the sum of all distributions
      const totalPercentage = this.form.distributions.reduce(
        (total, distribution) => {
          return total + parseFloat(distribution.percentage);
        },
        0,
      );

      if (totalPercentage !== 100) {
        this.error = "The sum of all distributions must be 100%";
        return;
      }

      this.saving = true;

      // Make the updated_at value show the current date
      const params = {
        id: this.id,
        name: this.form.name,
        distributions: this.form.distributions,
        updated_at: new Date().toLocaleString(),
      };

      // Timeout to show user that element is saving
      setTimeout(() => {
        this.$emit("edit", {
          id: params.id,
          name: params.name,
          distributions: params.distributions,
          updated_at: params.updated_at,
        });
        this.saving = false;
        this.display = true;
        this.error = ""; // Clear the error message after successful save
      }, 500);
    },

    // Added cancel method
    cancel() {
      // Reset form values
      this.getValuesFromProps();

      // Clear error message
      this.error = "";

      // Switch back to display mode
      this.display = true;
    },
  },
};
</script>

<style lang="scss">
@import "resources/scss/variables.scss";

.zone-editable {
  border: 1px solid $gray-color;
  padding: $qmb;
  border-radius: $border-radius;

  // New gray value, applied when hasManyDistributions is true
  &--gray {
    background-color: $gray-color;
  }

  .zone-display {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .zone-updated-at {
    display: flex;
    align-items: center;
    margin-left: auto;
    margin-right: 10px;
  }

  .zone-updated-at-text {
    margin-right: 0.5em;
    font-weight: bold;
    font-size: 8px;
  }

  .zone-updated-at-value {
    font-size: 12px;
  }

  .zone-edit {
    display: flex;
    flex-direction: column;
    gap: $small-action-space;

    .zone-edit-actions {
      display: flex;
      gap: $small-action-space;
      justify-content: end;
    }

    .zone-edit-distributions {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: $small-action-space;
    }
  }

  // New error message
  .error-message {
    color: red;
    margin-top: $small-action-space;
    font-size: 12px;
  }
}
</style>
