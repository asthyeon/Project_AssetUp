<template>
  <div class="board-container">
    <h1>게시판</h1>
    <hr>
    <RouterLink v-if="userStore.isLogin" :to="{ name: 'article_create' }" class="create-link">
      [CREATE]
    </RouterLink>
    
    <div v-if="store.articles.length > 0">
      <ArticleList :articles="store.articles" />
    </div>
    <div v-else>
      <h3 class="no-articles-message">글이 없습니다.</h3>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()
const userStore = useUserStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.board-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.create-link {
  margin-bottom: 10px;
  display: inline-block;
  text-decoration: none;
  padding: 5px 10px;
  background-color: #3498db;
  color: #fff;
  border-radius: 5px;
}

.no-articles-message {
  color: #888;
}
</style>