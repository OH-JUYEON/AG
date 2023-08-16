/*게시글 목록*/
showList();

function showList(){
	console.log(posts);
	posts = JSON.parse(posts);
	
	//files = JSON.parse(files);
	const $ul = $("#content-wrap ul");
	let text = "";
	
	posts.forEach(post => {
		text += `
			<li class="feed-item">
				<a class="soomgo-life-feed-item" href="javascript:location.href='${contextPath}/QnAListDetail.post?postId=${post.postId}'">
					<div class="feed-content service-address-info">
						<div>
							<section class="item-wrapper">
								<h3 class="sg-text-subhead5 sg-font-medium sg-text-gray-900">${post.postType}</h3>
								<p class="content sg-text-body2 sg-font-regular sg-text-gray-500">${post.postName}</p>
							</section>
						</div>
						<img src="https://static.cdn.soomgo.com/upload/media/698917af-7966-4cfb-b820-812eed2c2692.jpg?h=80&w=80&webp=1">
					</div>
					<div class="feed-footer">
						<div class="user-interaction">
							<span
								class="like sg-text-description sg-font-regular sg-text-gray-300">조회 수 ${post.postViewCount}</span>
							<span class="comment sg-text-description sg-font-regular sg-text-gray-300">댓글 수 ${post.postViewCount}</span>
						</div>
						<span class="sg-text-description sg-font-regular sg-text-gray-300"> ` + elapsedTime(post.postRegisterDate) +` </span>
					</div>
				</a>
			</li>
			`;
	});
	
	if(posts.length == 0){
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

/*let page = 1;
showList();

$(window).scroll(function(){
	//if ($(window).scrollTop() == $(document).height() - $(window).height()) {
	if (Math.ceil(window.innerHeight + window.scrollY) >= document.body.scrollHeight) {
		page++;
		showList();
	}
});

/*function showList(){
	$.ajax({
		url: contextPath + `/QnAListScrollOk.scroll?page=${page}`,
		dataType: "json",
		success: function(replies){
			let text = "";
	
			replies.forEach(post => {
				text += `
					<li class="feed-item">
						<a class="soomgo-life-feed-item" href="javascript:location.href='${contextPath}/QnAListDetail.post'">
							<div class="feed-content service-address-info">
								<div>
									<section class="item-wrapper">
										<h3 class="sg-text-subhead5 sg-font-medium sg-text-gray-900">${post.postType}</h3>
										<p class="content sg-text-body2 sg-font-regular sg-text-gray-500">${post.postName}</p>
									</section>
								</div>
								<img src="https://static.cdn.soomgo.com/upload/media/698917af-7966-4cfb-b820-812eed2c2692.jpg?h=80&w=80&webp=1">
							</div>
							<div class="feed-footer">
								<div class="user-interaction">
									<span
										class="like sg-text-description sg-font-regular sg-text-gray-300">조회 수${post.postViewCount}</span>
									<span class="comment sg-text-description sg-font-regular sg-text-gray-300">댓글 수${post.postViewCount}</span>
								</div>
								<span class="sg-text-description sg-font-regular sg-text-gray-300"> ` + elapsedTime(post.postRegisterDate) +` </span>
							</div>
						</a>
					</li>
					`;
			});
			
			$("#content-wrap ul").append(text);				
		}
	});
}
*/















