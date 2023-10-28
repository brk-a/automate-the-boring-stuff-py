import { useContext } from 'react'
import { TaskContext } from './context/taskContext'
import './App.css'
import TabList from './components/TabList'
import NewItem from './components/NewItem'

const App = () => {
  const {newItem} = useContext(TaskContext)
  return (
    <>
      <main className='context'>
        <h1 className='text-black text-uppercase text-center my-4'>
          FN Task Manager
        </h1>
        <div className='row'>
          <div className='col-md-6 col-sma-10 mx-auto p-0'>
            <div className='card p-3'>
              <div>
                <button className='btn btn-primary'>
                  Add task
                </button>
              </div>
              <TabList/>
              <ul className='list-group list-group-flush'>
              {newItem.map((item, i) => (
                <NewItem item={item} key={i}/>
              ))}
              </ul>
            </div>
          </div>
        </div>
      </main>
    </>
  )
}

export default App
