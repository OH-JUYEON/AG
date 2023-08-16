//let page = 1;
showList();

/*$(window).scroll(function(){
	//if ($(window).scrollTop() == $(document).height() - $(window).height()) {
	if (Math.ceil(window.innerHeight + window.scrollY) >= document.body.scrollHeight) {
		page++;
		showList();
	}
});*/


function showList(){
	$.ajax({
		
		url: contextPath + `/commentListOk.comment?postId=${postId}`,
		dataType: "json",
		success: function(replies){
			let text = "";
			
			replies.forEach(post => {
				text += `
					<li class="post-comments-list-item">
						<div class="post-comment-wrapper">
							<div class="profile-image provider">
								<img class="image" src="https://static.cdn.soomgo.com/upload/profile/89c0eaab-67ef-4897-938d-0bfa3f67e6d7.jpg?h=110&w=110">
							</div>
							<div class="comment-information">
								<div class="user-info provider">
									<div class="user-info-wrapper pro-user">
										<div class="user">
											<span class="user-name sg-text-subhead4 sg-font-bold sg-text-gray-900">${post.memberNickName}</span>
										</div>
									</div>
									<button class="send-request-button sg-text-subhead7 sg-font-medium">글 삭제</button>
								</div>
								<div class="content">
									<p class="text sg-text-body2 sg-font-regular">
										<span>A : ${post.commentContent}</span>
									</p>
								</div>
								<div class="comment-action-group sg-text-description sg-font-regular">
									<div class="comment-react">
										<span class="text"> ` + elapsedTime(post.commentRegisterDate) +`</span>
										<span class="divider-dot">·</span>
										<div class="like-area">
											<span>좋아요 0</span>
										</div>
									</div>
								</div>
							</div>
						</div>
					</li>
				`;
			});
			
			$("#content-wrap").append(text);				
		}
	});
}
