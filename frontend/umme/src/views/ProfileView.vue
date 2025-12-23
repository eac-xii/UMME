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

    <!-- 로그아웃 버튼 -->
    <!-- <button class="btn btn-danger" @click.prevent="logOut">로그아웃</button>
    <button v-if="!account.user?.is_spotify" class="btn btn-success" @click.prevent="connectSpotify">스포티파이 연동하기</button> -->
  </div>
</template>

<script setup>
import UserInfo from '@/components/Profile/UserInfo.vue'
import ThreadGrid from '@/components/Profile/ThreadGrid.vue'
import UserType from '@/components/Profile/UserType.vue'
import Playlist from '@/components/Profile/Playlist.vue'

const logOut = async () => {
  await account.logOut()
  router.push({ name: 'login' })
}

const connectSpotify = () => {
  account.connectSpotify()
}
</script>

<style scoped>
.first {
  height: 20rem;
}

.second {
  height: 30rem;
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
  padding: 10px;
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

