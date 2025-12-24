<template>
  <div class="row profile-container ms-2 me-1">
    <div class="col">
      <div class="row profile-top p-5">
        <span class="profile-image" :style="{ backgroundImage: `url('${userInfo?.image ? base_url + userInfo.image : defaultUser}')` }">
        </span>
        <div class="col profile-spotify">
          <span>{{ userInfo?.user?.is_spotify ? 'Spotify User' : 'Free User' }}</span>
        </div>
      </div>
      <div class="row profile-bottom">
        <div class="col-8 pt-3 ps-5">
          <span class="profile-name">{{ userInfo?.user?.last_name }} {{ userInfo?.user?.first_name }}</span>
          <br>
          <span class="profile-content">{{ userInfo?.content }}</span>
        </div>
        <div class="col-4 d-flex justify-content-end align-items-end pe-5 pb-3">
          <button v-if="userInfo?.user?.pk === account.user?.pk" type="button"
            class="btn btn-outline-light rounded-pill" data-bs-toggle="modal" data-bs-target="#editProfileModal" ref="editBtn">
            Edit profile
          </button>
        </div>
      </div>
    </div>
  </div>
  <div id="editProfileModal" class="modal fade" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">{{ userInfo?.user?.last_name }} {{
            userInfo?.user?.first_name }}'s profile</h1>
        </div>
        <div class="modal-body">
          <form>
            <div>
              <label for="introduction" class="form-label">Introduction</label>
              <input type="text" id="introduction" class="form-control" v-model="uploadIntro">
            </div>
            <div>
              <label for="upload-image" class="form-label">Image</label>
              <input type="file" class="form-control" id="upload-image" @change="setUploadImage">
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-outline-dark" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-outline-light" @click="updateProfile">Save changes</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { Modal } from 'bootstrap'
import { useAccountStore } from '@/stores/accounts'
import defaultUser from '@/assets/default-user.png'

const base_url = import.meta.env.VITE_API_BASE_URL

const account = useAccountStore()

const props = defineProps({
  userId: String
})

const userInfo = ref(null)

const editBtn = ref(null)
const uploadIntro = ref('')
const uploadImage = ref('')

const setUploadImage = (event) => {
  uploadImage.value = event.target.files[0]
}

const updateProfile = async () => {
  const formData = new FormData()
  formData.append('content', uploadIntro.value)

  if (uploadImage.value) {
    formData.append('image', uploadImage.value)
  }

  await account.updateProfile(formData)
  userInfo.value = await account.getProfile(userInfo.value?.user?.pk)
  closeModal()
}

const closeModal = () => {
  const modalEl = document.getElementById('editProfileModal')
  
  document.activeElement?.blur()

  const modal = Modal.getOrCreateInstance(modalEl)
  modal.hide()
  editBtn.value?.focus()
}

const loading = ref(true)
const error = ref(false)
watch(
  () => props.userId,
  async id => {
    if (!id) return
    try {
      userInfo.value = await account.getProfile(id)
    } catch {
      error.value = true
    } finally {
      loading.value = false
    }
  },
  { immediate: true }
)

</script>

<style scoped>
.profile-container {
  height: 100%;
  border-radius: 3vh;
}

.profile-image {
  width: 10vh;
  height: 10vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  border-radius: 100%;
}

.profile-top {
  height: 60%;
  padding: 1vh;
  background: linear-gradient(to bottom, #121212, #000);
  border-top-left-radius: 3vh;
  border-top-right-radius: 3vh;
}

.profile-spotify {
  display: flex;
  justify-content: end;
  font-size: 2vh;
  font-weight: 400;
  color: #aaa;
}

.profile-bottom {
  height: 40%;
}

.profile-name {
  font-size: 2.5vh;
  font-weight: 400;
}

.profile-content {
  font-size: 1.5vh;
}

.modal-dialog {
  border-radius: 2vh;
}

.modal-content {
  background: linear-gradient(to bottom, #121212, #000);
  border-radius: 2vh;
  color: #aaa;
  font-weight: 300;
}
</style>
