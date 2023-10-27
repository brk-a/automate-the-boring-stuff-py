import './App.css'
import { HashRouter as Router, Routes, Route } from 'react-router-dom'
import { Header } from './components'
import { NotesListPage, NotePage } from './pages'


function App() {

    return (
        <Router>
            <div className='container dark'>
                <div className='app'>
                <Header />
                <Routes>
                    <Route path='/' exact component={NotesListPage} />
                    <Route path='/note/:id' component={NotePage} />
                </Routes>
                {/* <Routes>
                    <Route path='/note/:id' component={NotePage} />
                </Routes> */}
                </div>
            </div>
        </Router>
    )
}

export default App
