<template>
  <div>
    <h1>카카오 맵 보기</h1>
    <hr>
    <button @click="panTo">이동</button>
    <form @submit.prevent="updateMap">
      <select name="" id="" v-model="citySelected" @change="getDistrict(citySelected)">
        <option value="">시/도</option>
        <option 
          v-for="city in store.infos.result"
          :key="city.cd"
          :value="{ cd: city.cd, addr_name: city.addr_name}"
        >
          {{ city.addr_name }}
        </option>
      </select>
      <select name="" id="" v-model="districtSelected" @change="getAddress()">
        <option value="">시/군/구</option>
        <option 
          v-for="district in districts"
          :key="district.cd"
          :value="district.addr_name"
        >
          {{ district.addr_name }}
        </option>
      </select>
      <select name="" id="" v-model="bankSelected" @change="getAddress()">
        <option value="">전체</option>
        <option 
          v-for="company in financeStore.companys"
          :key="company.fin_co_no"
          :value="company.kor_co_nm"
        >
          {{ company.kor_co_nm }}
        </option>
      </select>
      <button type="submit">찾기</button>
    </form>
    <hr>
    <div id="map"></div>
    <hr>
  </div>
</template>
<style scoped>
#map {
  width: 500px;
  height: 500px;
}
</style>
<script>
import { ref } from 'vue'
import { useAddressStore } from '@/stores/address'
import { useFinanceStore } from '@/stores/finance'
import axios from 'axios'

export default {
  name: "KakaoMap", // 컴포넌트 이름 지정
  data() {
    return {
      // map 객체 설정
      map: null,
    };
  },
  setup() {
    const citySelected = ref('')
    const districts = ref(null)
    const districtSelected = ref('')
    const financeStore = useFinanceStore()
    const store = useAddressStore()
    const address = ref('')
    const bankSelected = ref('')

    // '구'를 얻는 함수
    const getDistrict = function (citySelected) {
      console.log(citySelected.cd);
      axios({
        method: 'get',
        url: `https://sgisapi.kostat.go.kr/OpenAPI3/addr/stage.json?accessToken=${store.token}&cd=${citySelected.cd}`
      })
      .then((res) => {
        districts.value = res.data.result
        console.log(districts.value);
      })
      .catch((err) => {
        console.log(err);
      })
    }

    // 검색할 주소 얻기
    const getAddress = function () {
      address.value = citySelected.value.addr_name + ' ' + districtSelected.value + ' ' + bankSelected.value
      console.log(address);
    }

    return {
      citySelected, 
      districts,
      districtSelected, 
      bankSelected,
      store,
      getDistrict,
      address,
      getAddress,
      financeStore,
    }

  },
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
      const mapContainer = document.getElementById('map'), // 지도를 표시할 div 
          mapOption = { 
              center: new kakao.maps.LatLng(37.501301, 127.039610), // 지도의 중심좌표
              level: 4 // 지도의 확대 레벨
          };

      // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
      const map = new kakao.maps.Map(mapContainer, mapOption);      

      // 마커가 표시될 위치입니다 
      var markerPosition  = new kakao.maps.LatLng(37.501301, 127.039610); 

      // 마커를 생성합니다
      var marker = new kakao.maps.Marker({
          position: markerPosition
      });

      // 마커가 지도 위에 표시되도록 설정합니다
      marker.setMap(map);      
    },

    // 지도 이동 함수
    panTo() {
      console.log(map);
      // 이동할 위도 경도 위치를 생성합니다 
      var moveLatLon = new kakao.maps.LatLng(33.450580, 126.574942);

      // 지도를 표시할 div와  지도 옵션으로  지도를 생성합니다
         
      
      // 지도 중심을 부드럽게 이동시킵니다
      // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
      new kakao.maps.panTo(moveLatLon);             
    }
  }
}

</script>

<!-- <template>
  <div>
    <h1>카카오 맵 보기</h1>
    <hr>
    <form @submit.prevent="updateMap">
      <select name="" id="" v-model="citySelected" @change="getDistrict(citySelected)">
        <option value="">시/도</option>
        <option 
          v-for="city in store.infos.result"
          :key="city.cd"
          :value="{ cd: city.cd, addr_name: city.addr_name}"
        >
          {{ city.addr_name }}
        </option>
      </select>
      <select name="" id="" v-model="districtSelected" @change="getAddress()">
        <option value="">시/군/구</option>
        <option 
          v-for="district in districts"
          :key="district.cd"
          :value="district.addr_name"
        >
          {{ district.addr_name }}
        </option>
      </select>
      <select name="" id="" v-model="bankSelected" @change="getAddress()">
        <option value="">전체</option>
        <option 
          v-for="company in financeStore.companys"
          :key="company.fin_co_no"
          :value="company.kor_co_nm"
        >
          {{ company.kor_co_nm }}
        </option>
      </select>
      <button type="submit">찾기</button>
    </form>
    <hr>
    <div id="map"></div>
    <hr>
  </div>
</template>
<style scoped>
#map {
  width: 500px;
  height: 500px;
}
</style>
<script>
import { ref } from 'vue'
import { useAddressStore } from '@/stores/address'
import { useFinanceStore } from '@/stores/finance'
import axios from 'axios'

export default {
  name: "KakaoMap", // 컴포넌트 이름 지정
  data() {
    return {
      // map 객체 설정
      map: null,
    };
  },
  setup() {
    const citySelected = ref('')
    const districts = ref(null)
    const districtSelected = ref('')
    const financeStore = useFinanceStore()
    const store = useAddressStore()
    const address = ref('')
    const bankSelected = ref('')

    // '구'를 얻는 함수
    const getDistrict = function (citySelected) {
      console.log(citySelected.cd);
      axios({
        method: 'get',
        url: `https://sgisapi.kostat.go.kr/OpenAPI3/addr/stage.json?accessToken=${store.token}&cd=${citySelected.cd}`
      })
      .then((res) => {
        districts.value = res.data.result
        console.log(districts.value);
      })
      .catch((err) => {
        console.log(err);
      })
    }

    // 검색할 주소 얻기
    const getAddress = function () {
      address.value = citySelected.value.addr_name + ' ' + districtSelected.value + ' ' + bankSelected.value
      console.log(address);
    }

    return {
      citySelected, 
      districts,
      districtSelected, 
      bankSelected,
      store,
      getDistrict,
      address,
      getAddress,
      financeStore,
    }

  },
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

      var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
          mapOption = {
              center: new kakao.maps.LatLng(37.501301, 127.039610), // 지도의 중심좌표
              level: 4 // 지도의 확대 레벨
          };  

      // 지도를 생성합니다    
      var map = new kakao.maps.Map(mapContainer, mapOption); 

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
              content: '<div style="width:150px;text-align:center;padding:6px 0;">멀티캠퍼스 역삼</div>'
          });
          infowindow.open(map, marker);

          // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
          map.setCenter(coords);
          console.log(coords);
        } 
      });    
      
      // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
      var infowindow = new kakao.maps.InfoWindow({zIndex:1});

      // 장소 검색 객체를 생성합니다
      var ps = new kakao.maps.services.Places(map); 

      // 카테고리로 은행을 검색합니다
      ps.categorySearch('BK9', placesSearchCB, {
        useMapBounds:true
      }); 

      // 키워드 검색 완료 시 호출되는 콜백함수 입니다
      function placesSearchCB (data, status, pagination) {
        console.log(data);
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
    updateMap() {
      const self = this

      // 주소-좌표 변환 객체를 생성합니다
      var geocoder = new kakao.maps.services.Geocoder();

      // 좌표
      const loc_y = ref(null)
      const loc_x = ref(null)

      // 주소로 좌표를 검색합니다
      geocoder.addressSearch(self.address, function (result, status) {

        // 정상적으로 검색이 완료됐으면 
        if (status === kakao.maps.services.Status.OK) {

          var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

          loc_y.value = result[0].y
          loc_x.value = result[0].x

          console.log(`이동좌표: ${loc_y.value}, ${loc_x.value}`);

          // 결과값으로 받은 위치를 마커로 표시합니다
          var marker = new kakao.maps.Marker({
            map: map,
            position: coords
          });

          // 인포윈도우로 장소에 대한 설명을 표시합니다
          var infowindow = new kakao.maps.InfoWindow({
              content: `<div style="width:150px;text-align:center;padding:6px 0;">${self.address}</div>`
          });
          infowindow.open(map, marker);

          // 지도의 중심을 결과값으로 받은 위치로 이동시킵니다
          map.setCenter(coords);
          console.log(`이동위치: ${coords}`);
        } 
      });

      // // 기존의 지도 객체를 업데이트
      // map.setCenter(new kakao.maps.LatLng(loc_y.value, loc_x.value));
      // map.setLevel(3);

      var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
          mapOption = {
              center: new kakao.maps.LatLng(loc_y.value, loc_x.value), // 지도의 중심좌표
              level: 5 // 지도의 확대 레벨
          };  

      // 지도를 생성합니다    
      var map = new kakao.maps.Map(mapContainer, mapOption); 

      // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
      var infowindow = new kakao.maps.InfoWindow({zIndex:1});

      // 장소 검색 객체를 생성합니다
      var ps = new kakao.maps.services.Places(map); 
          
      console.log(map);
      // 키워드 검색 완료 시 호출되는 콜백함수 입니다
      function placesSearchCB (data, status, pagination) {
        console.log(`검색좌표: ${loc_y.value}, ${loc_x.value}`);
        console.log(status);
        console.log(pagination);
        if (status === kakao.maps.services.Status.OK) {
          console.log(`검색좌표2: ${loc_y.value}, ${loc_x.value}`);
          console.log(data);
          for (var i=0; i<data.length; i++) {
              displayMarker(data[i]);    
          }       
        }
      }
      // 카테고리로 은행을 검색합니다
      ps.categorySearch('BK9', placesSearchCB, {
        y: loc_y.value,
        x: loc_x.value
      }); 


      // 지도에 마커를 표시하는 함수입니다
      function displayMarker(place) {
        console.log(place);
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
    }
  },
};
</script> -->