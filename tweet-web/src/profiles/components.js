import React from 'react'



export function UserLink(props) {
  const {username} = props

  const handleUserLink = (event) => {
    window.location.href = `/profile/${username}`
  }
  return <span className='pointer' onClick={handleUserLink}>
           {props.children}
       </span>
  
}

export function UserDisplay(props) {
  const {user, includeFullName, hideLink} = props
  const nameDisplay = includeFullName === true ? `${user.first_name} ${user.last_name}` : null

  return <React.Fragment>
    {nameDisplay} {' '}
   {hideLink === true ? `@${user.username}` : <UserLink username={user.username}>@{user.username}</UserLink>}
  </React.Fragment>
}

export function UserPicture(props) {
  const {user, hideLink} = props
  const userIdspan = <span className="mx-1 px-3 py-2 rounded cirlce bg-dark text-white"> {user.username[0]} </span>
  
  return  hideLink === true ? userIdspan : <UserLink username={user.username}> {userIdspan} </UserLink>
}