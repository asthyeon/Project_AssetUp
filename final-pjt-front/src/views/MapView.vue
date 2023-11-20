<template>
  <div>
    <h1>카카오 맵 보기</h1>
    <hr>
    <div id="map"></div>
    <hr>
    <form>
      <select name="" id="">
        <option value="">시를 선택하세요.</option>
      </select>
      <select name="" id="">
        <option value="">구를 선택하세요.</option>
      </select>
      <select name="" id="">
        <option value="">은행을 선택하세요.</option>
      </select>
      <button>찾기</button>
    </form>
  </div>
</template>
<style scoped>
#map {
  width: 500px;
  height: 500px;
}
</style>
<script>
export default {
  name: "KakaoMap", // 컴포넌트 이름 지정
  data() {
    return {
      // map 객체 설정
      map: null,
    };
  },
  setup() {},
  created() {},
  mounted() {
  	// api 스크립트 소스 불러오기 및 지도 출력
    if (window.kakao && window.kakao.maps) {
      this.loadMap();
    } else {
      this.loadScript();
    }
  },
  unmounted() {},
  methods: {
  	// api 불러오기
    loadScript() {
      const script = document.createElement("script");
      const API_KEY = import.meta.env.VITE_KAKAO_API_KEY;
      script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${API_KEY}&libraries=services,clusterer,drawing&autoload=false`;
      script.onload = () => window.kakao.maps.load(this.loadMap); 

      document.head.appendChild(script);
    },
    // 맵 출력하기
    loadMap() {
// 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
var infowindow = new kakao.maps.InfoWindow({zIndex:1});

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(37.501301, 127.039610), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };  

// 지도를 생성합니다    
var map = new kakao.maps.Map(mapContainer, mapOption); 

// 장소 검색 객체를 생성합니다
var ps = new kakao.maps.services.Places(map); 

// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();

// 주소로 좌표를 검색합니다
geocoder.addressSearch('서울시 강남구 테헤란로 212', function(result, status) {

// 정상적으로 검색이 완료됐으면 
if (status === kakao.maps.services.Status.OK) {

    var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

    // 결과값으로 받은 위치를 마커로 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: coords
    });

    // 인포윈도우로 장소에 대한 설명을 표시합니다
    var infowindow = new kakao.maps.InfoWindow({
        content: '<div style="width:150px;text-align:center;padding:6px 0;">서울시 강남구 주변</div>'
    });
    infowindow.open(map, marker);

    // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
    map.setCenter(coords);
    console.log(coords);
} 
});    

// 카테고리로 은행을 검색합니다
ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true}); 

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {
        for (var i=0; i<data.length; i++) {
            displayMarker(data[i]);    
        }       
    }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x) 
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
}
    },
  },
};
</script>