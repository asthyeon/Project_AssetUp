<template>
  <div>
    <h3 @click="goBack">[Back]</h3>
    <h1>게시글 상세 보기</h1>
    <hr>
    <div v-if="store.articleDetail">
      <p>작성자 : {{ store.articleDetail.username }}</p>
      <p>제목 : {{ store.articleDetail.title }}</p>
      <p>내용 : {{ store.articleDetail.content }}</p>
      <p>작성일 : {{ store.articleDetail.created_at }}</p>
      <p>수정일 : {{ store.articleDetail.updated_at }}</p>
      <div>
        <p>좋아요 : {{ (store.articleDetail.like_authors || []).length }}</p>
      </div>
      <div v-if="store.articleDetail.username != store.name">
        <button @click="toggleLike">
          {{ likeButtonText }}
        </button>
      </div>
      <div v-if="store.articleDetail.username === store.name">
        <button @click="goUpdate">수정</button>
        <button @click="articleDelete">삭제</button>
      </div>
      <hr>
      <hr>
      <h4>댓글 목록</h4>
      <hr>
      <div>
        <CommentList 
          v-for="(comment, index) in store.articleDetail.comment_set"
          :key="comment.id"
          :comment="comment"
          :cnt="index + 1"
        />
      </div>
      <hr>
      <h4>댓글 작성</h4>
      <hr>
      <form @submit.prevent="commentCreate">
        <label for="content">댓글 : </label>
        <input type="text" v-model.trim="newComment" id="content">
        <input type="submit" value="작성">
      </form>
      <hr>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useCommentStore } from '@/stores/comment'
import { useUserStore } from '@/stores/user'
import { useRouter, useRoute } from 'vue-router'
import CommentList from '@/components/CommentList.vue'

const store = useArticleStore()
const commentStore = useCommentStore()
const userStore = useUserStore()
const route = useRoute()
const router = useRouter()
const newComment = ref('')
const cnt = ref(0)
const length = ref(0)

onMounted(() => {
  store.getArticleDetail(route.params.article_id)
  if (store.articleDetail.like_authors) {
    length.value = store.articleDetail.like_authors.length;
  }
})

// 게시글 업데이트 함수
const goUpdate = function () {
  router.push({ name: 'article_update', params: { article_id: route.params.article_id }})
}


// 게시글 삭제 함수
const articleDelete = function () {
  store.articleDelete(route.params.article_id)
}

// 좋아요 버튼 텍스트를 계산하는 computed 속성 추가
const likeButtonText = computed(() => {
  if (!store.articleDetail.like_authors) {
    return '좋아요'
  } else if (userStore.user.pk in store.articleDetail.like_authors) {
    return '좋아요 취소'
  } else {
    return '좋아요'
  }
});

// 좋아요 함수
const toggleLike = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/${route.params.article_id}/like/`,
    data: {
      is_liked: !store.articleDetail.like_authors.includes(store.name),
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);

      // 서버 응답에서 is_liked와 like_users 값을 반영
      store.articleDetail.like_authors = res.data.like_authors;

      // 좋아요 상태를 localStorage에 저장
      localStorage.setItem(`article_${route.params.article_id}_liked`, JSON.stringify(res.data.like_authors));

      // 반응형 변수인 length 업데이트
      length.value = res.data.like_authors.length;

    })
    .catch((err) => {
      console.log(err);
    });
}

// 댓글 작성 함수
const commentCreate = function () {
  commentStore.commentCreate(route.params.article_id, newComment.value)
  newComment.value = ''
  cnt.value += 1
}

// 뒤로 가기
const goBack = function () {
  router.back()
}


</script>

<style>

</style>
