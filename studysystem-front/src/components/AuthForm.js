import React from 'react'
import styles from '../styles/AuthForm.module.css'

const AuthForm = () => {
    return (
        <div className={styles.container}>
            <form action="http://localhost:8000/users/auth" method="POST" className={styles.login}>
                <p><b className={styles.login_header}>Login form</b></p>
                <p><input type="text" placeholder="username" className={styles.input_field}/></p>
                <p><input type="password" placeholder="password" className={styles.input_field}/></p>
                <p><input type="submit" value='Log In' className={styles.submit_button}/></p>
            </form>
        </div>
    )
}

export default AuthForm