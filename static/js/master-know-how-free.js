const $topic = $(".topic");
const $left_li = $("ul.topic li");
const $curation = $(".curation");


$left_li.on("click", function() {
	$curation.css("display", "none");
	$left_li.css("background", "none");
	$left_li.find("span").css("font-weight", "400");
	$left_li.find("span").css("color", "rgb(169, 169, 169");
	$(this).css("background", "#cabee3");
	$(this).find("span").css("font-weight", "700");
	$(this).find("span").css("color", "rgb(45, 45, 45)");
	if ($(this).attr('class') == "selected") {
		$curation.css("display", "block");
	}
});

/*배너 시작*/
const $prev = $(".slick-prev");		//앞으로가기
const $next = $(".slick-next");		//뒤로가기
const $track = $(".slick-track");	//베너 트렉
const $count = $(".curation-page");


$prev.on("click", function() {
	console.log("hi");
	$prev.css("display", "none");	//앞으로가기 버튼 안보이게하고
	$next.css("display", "block");	//뒤로가기 버튼 보이게하고
	$count.text("1/2");
	$track.css("transform", "translate3d(0px, 0px, 0px)");
	$track.css("transition", "0.7s");
});

$next.on("click", function() {
	console.log("hi");
	$next.css("display", "none");	//앞으로가기 버튼 안보이게하고
	$prev.css("display", "block");	//뒤로가기 버튼 보이게하고
	$count.text("2/2");
	$track.css("transform", "translate3d(-612px, 0px, 0px)");
	$track.css("transition", "0.7s");
});









/*게시글 목록*/

showList();

function showList(){
	console.log(KH);
	KH = JSON.parse(KH);
	//files = JSON.parse(files);
	const $ul = $("#content-wrap ul");
	let text = "";
	
	KH.forEach(board => {
		text += `
				<li class="feed-item"><a class="soomgo-life-feed-item"
						href="list-by-language-detail.jsp"> <!-- 목록 이름 -->
						<p
							class="topic-name sg-text-description sg-font-regular sg-text-gray-500">고수찾아요
								· 집 인테리어</p>
							<div class="feed-content service-address-info">
								<div>
									<section class="item-wrapper">
										<h3
											class="sg-text-subhead5 sg-font-medium sg-text-gray-900">드레스룸
											해체 및 이전설치조립 가능하신분</h3>
										<p
											class="content sg-text-body2 sg-font-regular sg-text-gray-500">
											이 제품 다른방으로 옮기려고하는데 해체하고 재조립 가능하신 고수님 계신가요</p>
									</section>
									<p
										class="sub-information sg-text-description sg-font-regular sg-text-gray-500">대전/중구</p>
								</div>
								<img
									src="https://static.cdn.soomgo.com/upload/media/698917af-7966-4cfb-b820-812eed2c2692.jpg?h=80&w=80&webp=1">
							</div>
							<div class="feed-footer">
								<div class="user-interaction">
									<span
										class="like sg-text-description sg-font-regular sg-text-gray-300">0</span>
									<span
										class="comment sg-text-description sg-font-regular sg-text-gray-300">0</span>
								</div>
								<span
									class="sg-text-description sg-font-regular sg-text-gray-300">방금 전</span>
							</div>
				</a></li>
			`;
	});
	
	if(KH.length == 0){
		text += `
			<li>
		        <div>
					현재 게시글이 없습니다. 게시글 작성을 해보세요!
				</div>
			</li>
		`
	}
	
	$ul.append(text);
}




















/*
autosize($("textarea"));

const $search = $("div.search-container input");
const $upload = $("input.upload");
const $thumbnail = $("label.attach img.thumbnail");
const $checkAgree = $("input[name='agree']");

$("img.preview").each(function(i){
    if(!$(this).attr("src")){
        $(this).hide();
    }
});

$search.on("focus", function(){
    $("div.search-container").css("outline", "#eb7c78 solid 2px");
});

$search.on("blur", function(){
    $("div.search-container").css("outline", "none");
});

$upload.on("change", function(e){
    let i = $upload.index($(this));
    var reader = new FileReader();
    reader.readAsDataURL(e.target.files[0]);
    reader.onload = function(e){
        let url = e.target.result;
        if(url.includes('image')){
            $("label.attach").eq(i).find("h6").hide();
            $("div.x").eq(i).show();
            $thumbnail.eq(i).show();
            $thumbnail.eq(i).attr('src', url);
        }else{
            showWarnModal("이미지 파일만 등록 가능합니다.");
        }
    }
});

$("div.x").on("click", function(e){
    e.preventDefault();
    let i = $("div.x").index($(this));
    $upload.eq(i).val("");
    $("label.attach").eq(i).find("h6").show();
    $("div.x").eq(i).hide();
    $thumbnail.eq(i).attr('src', "");
    $thumbnail.eq(i).hide();
});

$checkAgree.on("change", function(){
    let isChecked = $(this).prop("checked");
    isChecked ? checkedSaveId() : notCheckedSaveId();
});

function checkedSaveId(){
    $("#check-agree span.checkbox").css("border-color", "rgb(235 124 120)");
    $("#check-agree span.checkbox").css("background-color", "rgb(235 124 120)");
}

function notCheckedSaveId(){
    $("#check-agree span.checkbox").css("border-color", "");
    $("#check-agree span.checkbox").css("background-color", "");
}



/*정렬 이벤트 및 스타일 변경*/

/*
const $orders = $("section.order a");
$orders.on("click", function(e){
	let i = $orders.index(this);
	$form.find("input[name='sort']").val(i == 0 ? 'recent' : 'popular');
	$form.submit();
});

*/

/*시간 계산*/

/*
function elapsedTime(date) {
  const start = new Date(date);
  const end = new Date();

  const diff = (end - start) / 1000;
  
  const times = [
    { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
    { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
    { name: '일', milliSeconds: 60 * 60 * 24 },
    { name: '시간', milliSeconds: 60 * 60 },
    { name: '분', milliSeconds: 60 },
  ];

  for (const value of times) {
    const betweenTime = Math.floor(diff / value.milliSeconds);

    if (betweenTime > 0) {
      return `${betweenTime}${value.name} 전`;
    }
  }
  return '방금 전';
} 

*/