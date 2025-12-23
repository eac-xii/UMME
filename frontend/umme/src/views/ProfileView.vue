<template>
  <div class="container-fluid profile-layout px-5">
    <div class="row first">
      <div class="col-6 profile-overview">
        <div class="userinfo">
          <UserInfo />
        </div>
      </div>
      <div class="col-6  music">
        <div class="usertype">
          <UserType />
        </div>
      </div>
    </div>
    <div class="row second">
      <div class="col-6 profile-overview">
        <div class="threads">
          <ThreadGrid />
        </div>
      </div>
      <div class="col-6 music">
        <div class="playlist">
          <Playlist />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import UserInfo from '@/components/Profile/UserInfo.vue'
import ThreadGrid from '@/components/Profile/ThreadGrid.vue'
import UserType from '@/components/Profile/UserType.vue'
import Playlist from '@/components/Profile/Playlist.vue'
</script>

<style scoped>
.first {
  height: 24vh;
}

.second {
  height: 48vh;
}

.profile-layout {
  height: 100vh;
}

.profile-overview,
.music {
  min-width: 0;
}

.userinfo {
  height: 100%;
  padding: 10px;
}

.threads {
  height: 100%;
  overflow-y: scroll;
  padding: 10px;
}

.threads::-webkit-scrollbar {
  display: none;
}

.usertype {
  height: 100%;
  padding: 10px;
}

.playlist {
  height: 100%;
  padding: 10px;
}
</style>
