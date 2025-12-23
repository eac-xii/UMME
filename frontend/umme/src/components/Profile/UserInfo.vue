<template>
  <div class="card">
    <div class="profileImg"></div>
    <div id="user-meta" class="d-flex">
      <div class="userinfo mx-4 text-nowrap">
        <div id="name">{{ account.user.last_name }} {{ account.user.first_name }}</div>
        <div id="follow-info">Follower 30  |  Following 24</div>
      </div>
      <div class="followBtn">
        <button class="btn btn-dark">Follow</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from '@/stores/accounts'

const account = useAccountStore()

</script>

<style scoped>
.card {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  padding: 5rem;

  border-radius: 1rem;
  background-color: #121212;
  color: #aaa;
}

.profileImg {
  width: 6rem;
  aspect-ratio: 1;
  margin: 0 2%;
  background-color: aqua;
  border-radius: 50%;

  flex-shrink: 0;
  min-width: 48px;
  min-height: 48px;
}


#name {
  font-size: 2rem;
}

#follow-info {
  font-size: 1rem;
}
.followBtn {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 2rem;
}

.btn {
  width: 8rem;
}


/* .info {
  height: 70%;
  flex-grow: 1;
  margin: 0 2rem 0 0;
  padding: 1rem;
  align-items: center;
  flex-wrap: nowrap;
}

.buttons {
  margin-right: 1;
  width: 70%;
}
.btn {
  width: 5em;
  height: 1.5em;
  background-color: #121212;
} */
</style>
