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
