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

// flatpickr(픽업)
const dateSelector = document.querySelector('.dateSelector');
const timeSelector = document.querySelector('#timeSelector');

// 전송 form 관련 dom
// const app_carno = document.querySelector('#app_carno');
// const app_bymd = document.querySelector('#app_bymd');
// const app_carname = document.querySelector('#app_carname');
// const app_insptype = document.querySelector('#app_insptype');
// const app_expdate = document.querySelector('#app_expdate');
// const app_name = document.querySelector('#app_name');
// const app_tel1 = document.querySelector('#app_tel1');
// const app_tel2 = document.querySelector('#app_tel2');

// 신청데이타 초기화
let initData = ()=>{
	let app_carno = '';
	let app_bymd = '';
	let app_carname = '';
	let app_testype = '';
	let app_expdate = '';
	let app_name = '';
	let addr1 = '';
	let addr2 = '';
	let app_tel1 = '';
	let app_tel2 = '';
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


