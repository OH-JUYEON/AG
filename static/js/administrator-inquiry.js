showList();

function showList(){
	console.log(postes);
	postes = JSON.parse(postes);
	const $div = $(".board-list");
	let text = "";


	postes.forEach(post => {
		text += `
			<div class="post"><a href="administrator-inquiry-answer.jsp">
				<div class="checkbox"><input type="checkbox" name="postId" value="${post.postId}"></div>
				<div class="post-id">${post.postId}</div>
				<div class="post-name">${post.postName}</div>
				<div class="post-content">${post.postContent}</div>
				<div class="post-register-date">${post.postRegisterDate}</div>
				<div class="member-id">${post.memberId}</div>
				<div class="post-is-answered">${post.postIsBlinded}</div>
			</a></div>
			`;
	});
	
	$div.append(text);
	
}