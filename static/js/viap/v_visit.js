// dom 정의 (전역 사용)

// 다음주소 이용시
const daumPostcode = document.querySelector('#btnexecDaumPostcode')
const roadaddr = document.querySelector('#roadaddr')
const detailaddress = document.querySelector('#detailaddress')

// 자동차정보 입력
const loadTestInfo = document.querySelector('#loadTestInfo');
const carno = document.querySelector('#carno');
const bymd = document.querySelector('#bymd');
const testInfoSwitch = document.querySelector('#testInfoSwitch');
const carnomsg = document.querySelector('#carnomsg');
const subReqForm = document.submitReqForm;

// 검사대상일떄
const tsresult_car_name = document.querySelector('#tsresult_car_name')
const tsresult_test_type = document.querySelector('#tsresult_test_type')
const tsresult_exp_date = document.querySelector('#tsresult_exp_date')
const tsresultfee = document.querySelector('#tsresult_cost_1')
const tsresultagfee = document.querySelector('#tsresult_cost_2')
const tsresultpay = document.querySelector('#tsresult_payment')
const result_ts = document.querySelector('#result_ts')
const agentlist = document.querySelector('#agentlist')

// 검사대상이 아닐때
const carname_alt = document.querySelector('#carname_alert_display');
const expdate_alt = document.querySelector('#expdate_alert_display');
const alertdate_alt = document.querySelector('#alertdate_alert_display');

// 신청 관련 dom
const username = document.querySelector('#name');
const tel1 = document.querySelector('#tel1');
const tel2 = document.querySelector('#tel2');

const btnRstvnApp = document.querySelector('#btnRstvnApp');

// 신청데이타 초기화
let initData = ()=>{
	// 다음주소 이용시
	roadaddr.value = '';
	detailaddress.value = '';

	// 자동차정보 입력
	loadTestInfo.value = '';
	carno.value = '';
	carnomsg.value = '';

	// 검사대상일떄
	 tsresult_car_name.value = '';
	 tsresult_test_type.value = '';
	 tsresult_exp_date.value = '';
	 tsresultfee.value = '';
	 tsresultagfee.value = '';
	 tsresultpay.value = '';
	 result_ts.value = '';

	// 검사대상이 아닐때
	 carname_alt.value = '';
	 expdate_alt.value = '';
	 alertdate_alt.value = '';

	// 신청 관련 dom
	 username.value = '';
	 tel1.value = '';
	 tel2.value = '';

	// flatpickr(픽업)
	dateSelector.value = '';
	timeSelector.value = '';
// 	let app_carno = '';
// 	let app_bymd = '';
// 	let app_carname = '';
// 	let app_testype = '';
// 	let app_expdate = '';
// 	let app_pdate = '';
// 	let app_ptime = '';
// 	let app_name = '';
// 	let app_addr1 = '';
// 	let app_addr2 = '';
// 	let app_tel1 = '';
// 	let app_tel2 = '';
// 	let msg = '';
// 	let fnames = '';
};
// 주소차기 : 다음
function findAddr(){
	new daum.Postcode({
        oncomplete: function(data) {

        	 console.log(data);

            // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.
            // 도로명 주소의 노출 규칙에 따라 주소를 표시한다.
            // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
            let roadAddr = data.roadAddress; // 도로명 주소 변수
            let jibunAddr = data.jibunAddress; // 지번 주소 변수
            // 우편번호와 주소 정보를 해당 필드에 넣는다.
            // document.getElementById('member_post').value = data.zonecode;
            if(roadAddr !== ''){
                document.getElementById("roadaddr").value = roadAddr;
            }
            else if(jibunAddr !== ''){
                document.getElementById("roadaddr").value = jibunAddr;
            }
        }
    }).open();
}  // 주소찾기

// 차량번호 유효성 체크 function
let checkCno = (cno) => {
    let len = 0;
    let sido = "";
    let cnoJong = "";
    let cnoUse = "";
    let num = "";

    try {
        if (cno != null) {
            len = cno.length;
            if (len == 7) {	// ex) 05주2312
                cnoJong = cno.substring(0, 2);
                cnoUse = cno.substring(2, 3);
                num = cno.substring(3, 7);

                if (!isNaN(cnoJong) && isNaN(cnoUse) && !isNaN(num)) {
                    return 1;
                } else {
                    return 0;
                }
            } else if (len == 8) {	// ex) 1차점검 서울2사1234 --> 2차점검 999하9999
                sido = cno.substring(0, 2);
                cnoJong = cno.substring(2, 3);
                cnoUse = cno.substring(3, 4);
                num = cno.substring(4, 8);

                if (isNaN(sido) && !isNaN(cnoJong) && isNaN(cnoUse) && !isNaN(num)) {
                    return 1;
                } else {
                    //ex) 999하9999
                    cnoJong = cno.substring(0, 3);
                    cnoUse = cno.substring(3, 4);
                    num = cno.substring(4, 8);
                    if (!isNaN(cnoJong) && isNaN(cnoUse) && !isNaN(num)) {
                        return 1;
                    } else {
                        return 0;
                    }
                    //return 0;
                }
            } else if (len == 9) {	// ex) 서울52자1234
                sido = cno.substring(0, 2);
                cnoJong = cno.substring(2, 4);
                cnoUse = cno.substring(4, 5);
                num = cno.substring(5, 9);

                if (isNaN(sido) && !isNaN(cnoJong) && isNaN(cnoUse) && !isNaN(num)) {
                    if ("기,니,디,리,미,비,시,이,지,치".indexOf(cnoUse) != -1) {
                        return 2;
                    } else {
                        return 1;
                    }
                } else {
                    return 0;
                }
            } else {
                return 0;
            }
        } else {
            return 0;
        }
    } catch (e) {
        alert(e);
        return 0;
    }

    return 0;
};  // 차량번호 유효성 체크

// crsf_token function
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}  // crsf_token 쿠키

// 주소검색 function
function execDaumPostcode() {

	var themeObj = {
	   pageBgColor: "#FFFFFF", //페이지 배경색
	   outlineColor: "#FFFFFF" //테두리
	};
    // 현재 scroll 위치를 저장해놓는다.
    var currentScroll = Math.max(document.body.scrollTop, document.documentElement.scrollTop);

	var mapContainer = document.getElementById('map'), // 지도를 표시할 div
		mapOption = {
			//center: new daum.maps.LatLng(37.3996441086743, 126.970274096871), // 지도의 중심좌표
			center: new kakao.maps.LatLng(37.3996441086743, 126.970274096871), // 지도의 중심좌표
			level: 5 // 지도의 확대 레벨
		};

	//주소-좌표 변환 객체를 생성
	var geocoder = new daum.maps.services.Geocoder();
	//마커를 미리 생성
	//var marker = new daum.maps.Marker({
	//	position: new daum.maps.LatLng(37.3996441086743, 126.970274096871),
	//	map: map
	//});

    new daum.Postcode({
		theme: themeObj,
		animation: true,
        oncomplete: function(data) {

			//자동차검사는 주소입력이 가장 첫단계이므로, 기존에 입력된 값들을 초기화 한다
			$("#detailaddress").val('');
			carInfo.initTestInfo();

			//console.log("--------------------------------------");
			//console.log(data);

			// 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

			// 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
			var zipcode				=	"";		//우편번호
			var roadaddr				=	"";		//도로명주소
			var jibunaddr				=	"";		//지번주소1
			var autoJibunAddress	=	"";		//지번주소2
			var detailaddress		=	"";		//기타주소
			var building_name		=	"";		//건물명
			var sido						=	"";
			var gugun					=	"";
			var dong					=	"";

			zip_code				=	data.zonecode;
			roadaddr				=	data.roadAddress;			// 도로명 주소 변수
			jibunaddr				=	data.jibunAddress;			// 지번 주소 변수
			autoJibunAddress	=	data.autoJibunAddress;	// 지번 주소 변수
			sido						=	data.sido;
			sido						=	sido.replace("제주특별자치도", "제주");
			sido						=	sido.replace("세종특별자치시", "세종");

			if (sido == "세종") {
                gugun				=	"세종시";
			} else {
				if (data.sigungu !== ''){
					gugun				=	data.sigungu;
				} else {
					gugun				=	data.bname1;
				}
			}

			// 법정동명이 있을 경우 추가한다. (법정리는 제외) 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
            if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
				dong					=	data.bname;
				detailaddress		+=	data.bname;
            } else {
				dong					=	data.bname1;
				detailaddress		+=	data.bname2;
			}

            // 건물명이 있고, 공동주택일 경우 추가한다.
            if(data.buildingName !== '') {// && data.apartment === 'Y'){
				detailaddress				+= (detailaddress !== '' ? ', ' + data.buildingName : data.buildingName);
            }
            // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
            if(detailaddress !== ''){
                detailaddress = '(' + detailaddress + ')';
            }

			// 우편번호와 주소 정보를 해당 필드에 넣는다.
			$(" input[name=zipcode]").val(zip_code);
			$(" input[name=roadaddr]").val(roadaddr + ' '+ detailaddress);

			if (jibunaddr != '') {		//지번주소가 공백이 아니면
				$(" input[name=jibunaddr]").val(jibunaddr);
			} else {
				if (autoJibunAddress != '') {		//지번주소가 공백이 아니면
					jibunaddr				=	autoJibunAddress;			// 지번 주소 변수
					$(" input[name=jibunaddr]").val(jibunaddr);
				} else {
					$(" input[name=jibunaddr]").val(roadaddr);
				}
			}

			if (data.jibunAddressEnglish != '') {		//지번주소가 공백이 아니면
				var afterStr				= (data.jibunAddressEnglish).split(',');	//지번주소의 첫번째 값 번지 사용
			} else {
				var afterStr				= (data.autoJibunAddressEnglish).split(',');	//지번주소
			}
			$("input[name=car_location]").val(afterStr[0]);

			// 참고항목 문자열이 있을 경우 해당 필드에 넣는다.

			$(" input[name=sido]").val(sido);
			$(" input[name=gugun]").val(gugun);
			$(" input[name=dong]").val(dong);
			$(" input[name=pickup_address]").val(sido + ' '+gugun + ' '+dong);

			var stype				= 	$(" input[name=h_stype]").val();
			var car_maker_type	= 	$(" input[name=h_car_maker_type]").val();

			// 카카오지도API 주소-좌표 변환 객체를 생성합니다
			var geocoder = new daum.maps.services.Geocoder();

			// 주소로 좌표를 검색합니다
			geocoder.addressSearch(roadaddr, function(result, status) {

				// 정상적으로 검색이 완료됐으면
				if (status === daum.maps.services.Status.OK) {
					var coords = new daum.maps.LatLng(result[0].y, result[0].x);
					//console.log("--------------------------------------");
					//console.log(coords);
					//alert('ib='+coords.ib + 'jb='+coords.jb);

					//위경도 좌표입니다.
					$(" input[name=start_x]").val(result[0].y);
					$(" input[name=start_y]").val(result[0].x);

					if (!result[0].y || !result[0].x ) {
						Notify.alert({
							title : '알림',
							html : '선택하신 위치정보를 지도에 표시할 수 없습니다. 다시 시도하시거나 관리자에게 문의하세요',
							ok : function(){
							}
						});
						return;
					}

					$.ajax({
						type : "post",
						url : '/data.html?act=get_acode_visit',
						contentType : "application/x-www-form-urlencoded; charset=UTF-8",
						data : {
								"sido" : sido,
								"gugun" : gugun,
								"dong" : dong,
								"stype" : stype,
								"car_maker_type" : car_maker_type,
								"roadaddr" : roadaddr,
								"jibunaddr" : jibunaddr,
								"start_x"		: result[0].y,
								"start_y"		: result[0].x,
								"req_page"	: "visit_req"
						},
						dataType : "json",
						success : function(data) {
							if(data.code == 0){
								$(" input[name=h_acode]").val(data.list.acode);
								$(" input[name=h_cost2]").val(0);			//검사소방문은 대행료 0원
								$("#req_h_cost2").text(setComma(data.list.cost));	//대행을 할 경우 보여주기 위한 대행료
							}else{
								alert(data.message);
							}
						},
						error : function() {
							alert("정보 조회가 실패하였습니다.\n고객센터 1577-0266 또는 온라인상담에 서비스가 가능한 지역인지 확인을 요청해주세요");
						}
					});

				}
			});


			// 주소코드 가져오기 끝
			//$('#btnexecDaumPostcode > span').html('클릭해서 자동차 픽업주소를 입력하세요');


            // iframe을 넣은 element를 안보이게 한다.
            // (autoClose:false 기능을 이용한다면, 아래 코드를 제거해야 화면에서 사라지지 않는다.)
           // element_wrap.style.display = 'none';

            // iframe을 넣은 element를 안보이게 한다.
            // (autoClose:false 기능을 이용한다면, 아래 코드를 제거해야 화면에서 사라지지 않는다.)
            element_layer.style.display = 'none';

            // 우편번호 찾기 화면이 보이기 이전으로 scroll 위치를 되돌린다.
            document.body.scrollTop = currentScroll;
        },

		// 우편번호 찾기 화면 크기가 조정되었을때 실행할 코드를 작성하는 부분. iframe을 넣은 element의 높이값을 조정한다.
        onresize : function(size) {
            element_wrap.style.height = size.height+'px';
        },
        width : '100%',
        height : '100%',	//기본 100%인데, 로고가 가려지면 90%로 조정
        maxSuggestItems : 5
    //}).embed(element_wrap);
	}).embed(element_layer);

        // iframe을 넣은 element를 보이게 한다.
        //element_wrap.style.display = 'block';

// iframe을 넣은 element를 보이게 한다.
		element_layer.style.display = 'block';


        // iframe을 넣은 element의 위치를 화면의 가운데로 이동시킨다.
        initLayerPosition();
    // 브라우저의 크기 변경에 따라 레이어를 가운데로 이동시키고자 하실때에는
    // resize이벤트나, orientationchange이벤트를 이용하여 값이 변경될때마다 아래 함수를 실행 시켜 주시거나,
    // 직접 element_layer의 top,left값을 수정해 주시면 됩니다.
    function initLayerPosition(){
        var width = 300; //우편번호서비스가 들어갈 element의 width
        var height = 400; //우편번호서비스가 들어갈 element의 height
        var borderWidth = 1; //샘플에서 사용하는 border의 두께

        // 위에서 선언한 값들을 실제 element에 넣는다.
        element_layer.style.width = width + 'px';
        element_layer.style.height = height + 'px';
        element_layer.style.border = borderWidth + 'px solid';
        // 실행되는 순간의 화면 너비와 높이 값을 가져와서 중앙에 뜰 수 있도록 위치를 계산한다.
        element_layer.style.left = (((window.innerWidth || document.documentElement.clientWidth) - width)/2 - borderWidth) + 'px';
        element_layer.style.top = (((window.innerHeight || document.documentElement.clientHeight) - height)/2 - borderWidth) + 'px';
    }

} // 주소검색 종료

// 이미지 파일 첨부하기
$(document).ready(function(){
	$('input[type=file]').drop_uploader({
		uploader_text: '차량사진을 여기로 가져오거나 ',
		browse_text: '컴퓨터에서 찾기',
		only_one_error_text: 'Only one file allowed',
		not_allowed_error_text: '이미지 파일만 가능합니다',
		big_file_before_error_text: 'Files, bigger than',
		big_file_after_error_text: 'is not allowed',
		allowed_before_error_text: 'Only',
		allowed_after_error_text: 'files allowed',
		browse_css_class: 'btn btn-primary',
		browse_css_selector: 'file_browse',
		uploader_icon: '<i class="mdi mdi-tooltip-image-outline"></i>',
		file_icon: '<i class="pe-7s-file"></i>',
		progress_color: '#4a90e2',
		time_show_errors: 5,
		layout: 'thumbnails',
		method: 'normal',
		url: 'ajax_upload.php',
		delete_url: 'ajax_delete.php',
	});
});

$(document).on('click', '.btn_login_sns', function() {
	var sns = $(this).attr('data-type');
	if(sns == 'naver') {
		window.open('/plugins/sns/naver.php', 'sns', "width=600,height=350,resizable=yes,scrollbars=yes");
	}
});
function goNext(url) {
	location.href=url;
}

let agreeTerm = {
	//자동차검사정보 조회 동의
	testInfoChk : function(){
		if(!$('#testInfoSwitch').is(":checked")){
			if($('#h_ttype').val() !='') {
				if(confirm("검사기초 정보가 있습니다.\n\n동의를 해제할 경우 기존 정보가 초기화 됩니다.\n\n진행 하시겠습니까?")) {
					$('.mk').prop('checked', false).val("");
					$('.mk').next('label').removeClass("selected");
					//기존 검사정보 초기화
					carInfo.initTestInfo();
				}
			} else {
				$('.mk').prop('checked', false).val("");
				$('.mk').next('label').removeClass("selected");
			}
		}else{
			$('.mk').prop('checked', true).val("Y");
			$('.mk').next('label').addClass("selected");
		}
	},

	//자동차검사안내 Layer 동의
	alertChk : function(){
		if(!$('#alertChk').is(":checked")){
			$('.alert').prop('checked', false).val("");
			$('.alert').next('label').removeClass("selected");
		}else{
			$('.alert').prop('checked', true).val("Y");
			$('.alert').next('label').addClass("selected");
		}
	},

	// 전체 동의
	termAllChk : function(){
		if(!$('#termAllChk').is(":checked")){
			$('.term').prop('checked', false).val("");
			$('.term').next('label').removeClass("selected");
		}else{
			$('.term').prop('checked', true).val("Y");
			$('.term').next('label').addClass("selected");
		}
	},
	termChk : function(id){
		if(!$('#'+id).is(":checked")){
			$('#'+id).val("");
			$('#'+id).next("label").removeClass("selected");

			$('#termAllChk').prop('checked', false).val("");
			$('#termAllChk').next('label').removeClass("selected");
		}else{
			$('#'+id).val("Y");
			$('#'+id).next("label").addClass("selected");
		}
	},

	openUserInfo : function(){
		window.scrollTo(0,0);
		$('#userInfoLayer').show();
	},
	closeUserInfo : function(){
		$('#userInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-110}, 1200);
	},
	openPrivacyInfo : function(){
		window.scrollTo(0,0);
		$('#privacyInfoLayer').show();
	},
	closePrivacyInfo : function(){
		$('#privacyInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-110}, 1200);
	},
	openNoticeInfo : function(){
		window.scrollTo(0,0);
		$('#noticeInfoLayer').show();
	},
	closeNoticeInfo : function(){
		$('#noticeInfoLayer').hide();
		//약관확인 후 약관 위치로 이동
		var offset = $("#testagreement").offset();
		$('html, body').animate({scrollTop : offset.top-110}, 1200);
	}
};


