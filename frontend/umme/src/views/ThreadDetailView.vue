<template>
  <div class="thread-detail-container">
    <!-- Left: Album / Track Info -->
    <div class="track-card">
      <img :src="thread.track?.image" class="album-cover" alt="Album Cover" />
      <div class="track-info">
        <p class="album-name">{{ thread.track?.album }} {{ thread.track?.year }}</p>
        <h2 class="track-title">{{ thread.track?.name }}</h2>
        <p class="artist-name">{{ thread.user?.first_name }}</p>
      </div>
    </div>

    <!-- Right: Thread Content + Likes/Comments + Replies -->
    <div class="thread-content">
      <p class="time">{{ thread.timeAgo }}</p>
      <p class="content">{{ thread.content }}</p>

      <div class="engagement">
        <button class="like-btn"><i class="bi bi-heart"></i> {{ likesCount }}</button>
        <button class="comment-btn"><i class="bi bi-chat"></i> {{ comments.length }}</button>
      </div>

      <!-- 댓글 목록 -->
      <div class="comments">
        <div v-for="comment in comments" :key="comment.id" class="comment-item">
          <div class="avatar">{{ comment.user?.first_name[0] }}</div>
          <div class="comment-body">
            <strong>{{ comment.user?.first_name }} {{ comment.user?.last_name }}</strong>
            <p>{{ comment.content }}</p>
          </div>
        </div>
      </div>

      <!-- 댓글 입력 -->
      <div class="comment-input-section">
        <div class="avatar current-user">T</div>
        <input
          type="text"
          v-model="newComment"
          placeholder= "Reply to ..."
          @keyup.enter="postComment"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '@/api/axios'

const route = useRoute()
const threadId = route.params.id

const thread = ref({})
const comments = ref([])
const newComment = ref('')
const likesCount = ref(0)

const fetchThread = async () => {
  try {
    const res = await api.get(`/threads/${threadId}`)
    thread.value = res.data
    likesCount.value = res.data.likes_count || 0
  } catch (err) {
    console.error(err)
  }
}
onMounted(async () => {
  await fetchThread()
})
</script>

<style scoped>
.thread-detail-container {
  display: flex;
  margin: 3rem;
  gap: 2rem;
  background-color: #121212;
  padding: 3rem;
  border-radius: 1rem;
  color: #aaa;
  height: 40rem;
}

/* Left Column: Album */
.track-card {
  padding: 0 2rem;
  width: 300px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.album-cover {
  width: 100%;
  border-radius: 1rem;
  object-fit: cover;
}
.track-info .album-name {
  font-size: 0.85rem;
  color: #b3b3b3;
}
.track-info .track-title {
  font-size: 1.5rem;
  color: #1ed760;
  margin: 0.3rem 0;
}
.track-info .artist-name {
  font-size: 1rem;
  color: #aaa;
}

/* Right Column: Thread Content */
.thread-content {
  flex: 1;
}
.time {
  font-size: 0.8rem;
  color: #b3b3b3;
  margin-bottom: 0.5rem;
}
.content {
  font-size: 1rem;
  margin-bottom: 1rem;
  white-space: pre-wrap;
}
.engagement {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}
.like-btn, .comment-btn {
  background: transparent;
  border: none;
  color: #b3b3b3;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}
.like-btn:hover, .comment-btn:hover {
  color: #1ed760;
}

/* 댓글 */
.comments {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1rem;
}
.comment-item {
  display: flex;
  gap: 1rem;
}
.comment-item .avatar {
  width: 40px;
  height: 40px;
  background-color: #333;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
  color: #1ed760;
}
.comment-body p {
  margin: 0;
  color: #aaa;
}

/* 댓글 입력 */
.comment-input-section {
  display: flex;
  gap: 1rem;
  align-items: center;
}
.comment-input-section .avatar.current-user {
  display: flex;
  background-color: #1ed760;
  color: #121212;
  width: 2rem;
  aspect-ratio: 1;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  font-weight: 600;
}
.comment-input-section input {
  flex: 1;
  background-color: #1e1e1e;
  border: none;
  border-radius: 999px;
  padding: 0.5rem 1rem;
  color: #aaa;
}
.comment-input-section input:focus {
  outline: none;
  background-color: #2a2a2a;
}
</style>
