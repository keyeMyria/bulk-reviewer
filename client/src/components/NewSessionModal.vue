<template>
  <div class="modal is-active">
    <div class="modal-background" @click="close"></div>
    <div class="modal-card">
      <header class="modal-card-head">
        <p class="modal-card-title">Create New Session</p>
        <button class="delete" aria-label="close" @click="close"></button>
      </header>
      <section class="modal-card-body">
        <!-- Form validation errors -->
        <alert :message="errorMessages" @hideMessage="hideErrorAlertMessage" v-show="errorMessages.length > 0" class="is-danger"></alert>
        <!-- Form upload success -->
        <alert :message="successMessage" @hideMessage="hideSuccessAlertMessage" v-show="showSuccess" class="is-success"></alert>
        <!-- Form -->
        <form id="new-session-form">
          <!-- Name -->
          <div class="field">
            <label class="label">Name</label>
            <div class="control input-container">
              <input class="input" type="text" name="name" v-model="name" placeholder="Name">
            </div>
          </div>
          <!-- Source path -->
          <div class="field">
            <label class="label">Source</label>
            <div class="control input-container">
              <input class="input" type="text" name="source" v-model="source" placeholder="/path/to/source">
            </div>
          </div>
          <!-- Disk image -->
          <div class="field">
            <label class="label">Source type</label>
            <div class="control">
              <div class="select">
                <select name="ssn" v-model="diskImage">
                  <option value=false>Directory</option>
                  <option value=true>Disk Image</option>
                </select>
              </div>
            </div>
          </div>
          <!-- Bulk Extractor profile -->
          <div class="field">
            <label class="label">Bulk Extractor profile</label>
            <div class="control">
              <div class="select">
                <select name="selectedConfig" v-model="selectedConfig">
                    <option v-for="config in configs" :value="config.uuid" :key="config.uuid">
                      {{ config.name }}
                    </option>
                </select>
              </div>
            </div>
          </div>
        </form>
      </section>
      <footer class="modal-card-foot">
        <button class="button is-success" :disabled="formSubmit" @click.prevent="processForm">Create</button>
        <button class="button" @click.prevent="clearForm">Clear</button>
      </footer>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Alert from '@/components/Alert'

export default {
  name: 'new-session-modal',
  components: { Alert },
  data () {
    return {
      formSubmit: false,
      errorMessages: [],
      name: '',
      source: '',
      diskImage: false,
      configs: [],
      selectedConfig: null,
      successMessage: 'Success!',
      showSuccess: false
    }
  },
  created () {
    this.getConfigs()
  },
  methods: {
    getConfigs: function () {
      axios.get(`http://127.0.0.1:8000/api/config/`)
        .then(response => {
          this.configs = response.data
        })
        .catch(e => {
          console.log(e)
        })
    },
    processForm: function () {
      // disable submit button
      this.formSubmit = true

      // form validation
      let formValidation = true
      if (!this.name) {
        this.errorMessages.push('Name value is required.')
        formValidation = false
      }
      if (this.name.length > 100) {
        this.errorMessages.push('Name must be less than 100 characters.')
        formValidation = false
      }
      if (!this.source) {
        this.errorMessages.push('Source is required.')
        formValidation = false
      }
      if (!this.selectedConfig) {
        this.errorMessages.push('Bulk Extractor configuration is required.')
        formValidation = false
      }
      if (formValidation === false) {
        this.formSubmit = false
        return
      }

      // set data
      let data = new FormData()
      data.append('name', this.name)
      data.append('source_path', this.source)
      if (this.diskImage === 'true') {
        data.append('disk_image', true)
      } else {
        data.append('disk_image', false)
      }
      data.append('be_config', this.selectedConfig)

      // POST form
      axios.post(`http://127.0.0.1:8000/api/session/add/`, data)
        .then(response => {
          console.log(response)
          this.showSuccess = true
        })
        .catch(e => {
          console.log(e)
        })

      // re-enable submit button
      this.formSubmit = false
    },
    clearForm: function () {
      this.formSubmit = false
      this.name = ''
      this.source = ''
      this.diskImage = false
      this.selectedConfig = null
      this.errorMessages = []
      this.showSuccess = false
    },
    hideErrorAlertMessage: function () {
      this.errorMessages = []
    },
    hideSuccessAlertMessage: function () {
      this.showSuccess = false
    },
    close: function () {
      this.clearForm()
      this.$emit('newSessionClose')
    }
  }
}
</script>

<style>
</style>
