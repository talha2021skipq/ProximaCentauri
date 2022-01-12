//<<<<<<<<<< Importing the required librariess >>>>>>
import { Flex, Box,ListItem, UnorderedList, Text, Heading, VStack, Button,Spacer } from '@chakra-ui/react';
import { Input, Image } from '@chakra-ui/react'
import React, {useState, useEffect} from 'react';
import axios from 'axios'
import ReactPaginate from 'react-paginate';
// Main App unction to return a V-stack
function App() {
  const [data, setData]=useState(null);
  const [print, setPrint]= useState(false);
  const [put, setPut]= useState(false);
  const [del, setDel]= useState(false);
  const [urltoput, setUrltoput]= useState(null);
  const [urltodel, setUrltodel]= useState(null);

  const urls=["talha", "ali", "umar"];
  const [posts, setPosts]= useState([]);
  const [loading, setLoading]= useState(false);
  const [currentPage, setCurrentPage]= useState(1);
  const [postsPerPage, setPostsPerPage]= useState(10);
  useEffect(() => 
  {
    const fetchPosts= async() => 
    {
      setLoading(true);
      const res=await axios({method: 'GET',headers: { 'Content-Type': 'application/json' },url:"https://n0q8c9iur5.execute-api.us-east-2.amazonaws.com/prod/"});
      setPosts(res.data);
      setLoading(false);
    }
    fetchPosts();
  },[]);
  console.log("New")
  const [condition, setcondition]= useState(false);
  console.log(posts);
  const items = posts 
//<<<<<<<<<<< Function to collect the url that is to be put>>>>>>>>>>>>>>
function putData(val)
{

  setUrltoput(val.target.value)
  
}
//<<<<<<<<<<< Function to collect the url that is to be deleted>>>>>>>>>>>>>>
function delData(val)
{

  setUrltodel(val.target.value)
  
}
////<<<<<<<<<<<<<<<<<Function to del url from DB>>>>>>>>>>>>>>>>>>>>>>>>>>>
function delurl()
{
  const res= axios({method: 'DELETE',
  headers:  {  },
  url:"https://n0q8c9iur5.execute-api.us-east-2.amazonaws.com/prod/" , 
  data: urltodel});
//setPosts(res.data);
 setLoading(false);
 console.log(res);
 setDel(true);
}
//<<<<<<<<<<< Function to PUT the url that was collected>>>>>>>>>>>>>>
function saveurl()
{
  const res= axios({method: 'PUT',
  headers:  {  },
  url:"https://n0q8c9iur5.execute-api.us-east-2.amazonaws.com/prod/" , 
  data: urltoput});
//setPosts(res.data);
 setLoading(false);
 console.log(res);
 setPut(true);
}


//<<<<<<<<<<<<<<<<<<<<<<<<< Search in the data>>>>>>>>>>>>>>>>>
  function getData(val)
  {
    var dans="";
    for (const el of items)
    {
      if (val.target.value ==el)
      {
        dans="The URL is found in the Dynamodb database.";
        break;
      }
      else
      {
        dans="Sorry! The URL is not found in our database. It's either never added or has been deleted.";
      }
    }

    setData(dans)
    setPrint(false)
    console.warn(val.target.value)
  }

// Pagination
//const items =  ['www.ieee.org','www.skipq.org','www.namal.edu.pk','www.hulu.com','www.icecet.org', 'www.nust.edu.pk', 'www.paf.gov.pk', 12, 13, 14];



//<<<<<<<<<<<<<<<<<< Print Items(URLS) as unordered list in the pagination>>>>>>>>>>>>
function Items({ currentItems }) {
  return (
    <>
      {currentItems &&
        currentItems.map((item) => (
         
          <Box w='100%'>
          <UnorderedList>  
           <ListItem> {item}</ListItem>
          </UnorderedList>
          </Box> )
          )
        }
        </>
    
  );
}
////<<<<<<<<<<<<<<<<<<<<Get items to be shown on one page >>>>>>>>>>>>>>
function PaginatedItems({ itemsPerPage }) 
{
  // We start with an empty list of items.
  const [currentItems, setCurrentItems] = useState(null);
  const [pageCount, setPageCount] = useState(0);
  const [itemOffset, setItemOffset] = useState(0);

  useEffect(() => {
    // Fetch items from another resources.
    const endOffset = itemOffset + itemsPerPage;
    console.log(`Loading items from ${itemOffset} to ${endOffset}`);
    setCurrentItems(items.slice(itemOffset, endOffset));
    setPageCount(Math.ceil(items.length / itemsPerPage));
  }, [itemOffset, itemsPerPage]);

  // Invoke when user click to request another page.
  const handlePageClick = (event) => {
    const newOffset = (event.selected * itemsPerPage) % items.length;
    console.log(
      `User requested page number ${event.selected}, which is offset ${newOffset}`
    );
    setItemOffset(newOffset);
  };

  return (
<VStack>
    <Flex>
    <Box>
      <Items currentItems={currentItems} />
      </Box>
    </Flex>
    <Flex >
      <ReactPaginate
        breakLabel="..."
        nextLabel="Next>" 
        onPageChange={handlePageClick}
        pageRangeDisplayed={5}
        pageCount={pageCount}
        previousLabel="<Back"
        renderOnZeroPageCount={null}
      />

    </Flex>
    </VStack>
  );
}
//<<<<<<<<<<<<<<<< Paginate unction ends here by returing a VSTACK>>>>>>>>>>>>>>>>>>>>>>
  return (
    <VStack>
      <Box variant='outline' bg='yellow.200'  w='100%' p={1} color='black' >
        <Text fontSize ="10" fontWeight ="semibold"> Talha Naeem DevOps Trainee @SkipQ </Text>
      </Box>

  <Flex>
        <Heading  color ='blue.210'  colorScheme='gray' fontSize="4xl" > User Interface for Web Crawler </Heading>
  </Flex>
        
  <Flex> 
        <Box variant='outline'  mr='15' ml= "15"  w='100%' p={2} color='black'>
        <Text> 
        The UI is for the web-crawler with which users can get data of URLs from database through API gateway. The UI is created with ReactJS Chakra UI library, and I have used AXIOS library to fetch data from my API. In the sprint4, I had to create a frontend using ReactJS. The frontend should have two features, show the URLs and to search a URL in the database. In reactJS, wen we have to use Chakra UI library. And we have to add a pagination for URLs display. In the end, we need Oauth authorization and then the react app is to be deployed at AWS Amplify.
        </Text> </Box> 
  </Flex>

  <Flex>
    <Image src='https://freepngdesign.com/content/uploads/images/p-1688-5-aws-dynamodb-logo-png-transparent-logo-839807569618.png' boxSize='200px' objectFit='cover' /> 
  </Flex>

    <Flex w='100%'>
      <Box variant='outline' bg='yellow.200'  w='100%' p={2} color='black' >
          <Text fontSize ="2xl" fontWeight ="semibold"> To Put URLs </Text>
       </Box>
    </Flex>

  <Flex>   
      <Box variant='outline' w='100%' p={2} color='black' >
        <Text fontSize ="1xl" > If you want to enter any URL in the database, you can enter the URL below and click on PUT. </Text>
      </Box>
  </Flex>
  
  <Flex>
    <Input mr ="3" placeholder='Enter URL to Put' type ="text" onChange={putData}/>      
  </Flex>
      
  <Flex> 
    <Button colorScheme='red' onClick={saveurl} >
    Put </Button>
  </Flex>

  <Flex >
      { put?
     <Box variant='outline' bg='gray' fontSize="1xl" p={2.5} color='white' borderWidth='1px' borderRadius='lg' > 
        The URL has been put, you may check. </Box> 
      :null
       }
  </Flex>

  <Flex w='100%'>
      <Box variant='outline' bg='yellow.200'  w='100%' p={2} color='black' >
          <Text fontSize ="2xl" fontWeight ="semibold"> To Delete URLs </Text>
       </Box>
  </Flex>

  <Flex>   
      <Box variant='outline' w='100%' p={2} color='black' >
        <Text fontSize ="1xl" > If you want to delete any URL in the database, you can enter the URL below and click on DELETE. </Text>
      </Box>
  </Flex>
      <Flex>

      <Input mr ="3" placeholder='Enter URL to Put' type ="text" onChange={delData}/>      
      </Flex>
      
  <Flex> 
    <Button colorScheme='red' onClick={delurl} >
    Delete </Button>
  </Flex>

  <Flex >
      { del?
     <Box variant='outline' bg='gray' fontSize="1xl" p={2.5} color='white' borderWidth='1px' borderRadius='lg' > 
        The URL has been deleted if it was in the database, you may check. </Box> 
      :null
       }
  </Flex>

  <Flex w='100%'>
      <Box variant='outline' bg='yellow.200'   w='100%' p={2} color='black' >
        <Text fontSize ="2xl" fontWeight ="semibold"> Search in the Database </Text>
      </Box>
  </Flex>
 
  <Flex>
        <Box variant='outline'   w='100%' p={2} color='black' >
          <Text fontSize ="1xl" > If you want to search any URL in the database, you can enter the URL beolw and click on Search URLs. </Text>
        </Box>
  </Flex>
      
  <Flex>
      <Input mr ="3" placeholder='Enter URL to Search' type ="text" onChange={getData}/>      
  </Flex>
  
  <Flex> 

    <Button colorScheme='red' onClick={()=> setPrint(true)} >
        Search </Button>
  </Flex>

  <Flex >
      { print?
        <Box variant='outline' bg='gray' fontSize="1xl" p={2.5} color='white' borderWidth='1px' borderRadius='lg' > {data} </Box> 
        :null
      }
  </Flex>
  
  <Flex w='100%'>
    <Box variant='outline' bg='yellow.200'  w='100%' p={2} color='black' >
      <Text fontSize ="2xl" fontWeight ="semibold"> To Show URLs </Text>
    </Box>
  </Flex>

  <Flex>
      <Box variant='outline'   w='100%' p={2} color='black' >
        <Text fontSize ="1xl" > If you want to see URLs which are located in the Dynamodb table, Click on the button below: </Text>
      </Box>
  </Flex>
      <Button  colorScheme='red' onClick={(t)=>  setcondition(true) } >
        Show Data </Button>
      
    <Flex>
      { condition?
        <PaginatedItems itemsPerPage={10} />
       :null
      }  
    </Flex>
 
  <Flex   >
        <Box mr='1150'>  <Text fontSize ="12"> 11/01/2022 ProximaCentauri, SkipQ</Text>
        </Box>
        </Flex><Flex>
      <Box mr='1200'> <Image src='https://www.skipq.org/public/images/logo.svg' boxSize='120px' /> 
        </Box>
  </Flex>


</VStack>

    );
}

export default App;
