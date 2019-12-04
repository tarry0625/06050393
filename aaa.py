[
    {
        "id": "28b6140b.f0ec6c",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "3a561f1f.85886",
        "type": "http in",
        "z": "28b6140b.f0ec6c",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 160,
        "y": 280,
        "wires": [
            [
                "3f7b243b.ac7a9c",
                "bc341dd8.b9e44"
            ]
        ]
    },
    {
        "id": "3f7b243b.ac7a9c",
        "type": "function",
        "z": "28b6140b.f0ec6c",
        "name": "set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 380,
        "wires": [
            [
                "2db55c33.d72b84"
            ]
        ]
    },
    {
        "id": "2db55c33.d72b84",
        "type": "rpi-gpio out",
        "z": "28b6140b.f0ec6c",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 640,
        "y": 480,
        "wires": []
    },
    {
        "id": "bc341dd8.b9e44",
        "type": "function",
        "z": "28b6140b.f0ec6c",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 400,
        "y": 40,
        "wires": [
            [
                "787665f9.79a2bc",
                "4037d959.803b28"
            ]
        ]
    },
    {
        "id": "787665f9.79a2bc",
        "type": "http response",
        "z": "28b6140b.f0ec6c",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 910,
        "y": 120,
        "wires": []
    },
    {
        "id": "4037d959.803b28",
        "type": "debug",
        "z": "28b6140b.f0ec6c",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 950,
        "y": 500,
        "wires": []
    },
    {
        "id": "7aea8ef3.19d2c",
        "type": "http in",
        "z": "28b6140b.f0ec6c",
        "name": "clear GPIO5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 180,
        "y": 660,
        "wires": [
            [
                "560fe7ce.0ae1d8",
                "3c32f160.6105ce"
            ]
        ]
    },
    {
        "id": "560fe7ce.0ae1d8",
        "type": "function",
        "z": "28b6140b.f0ec6c",
        "name": "clear yo 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 420,
        "y": 600,
        "wires": [
            [
                "2db55c33.d72b84"
            ]
        ]
    },
    {
        "id": "3c32f160.6105ce",
        "type": "function",
        "z": "28b6140b.f0ec6c",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 450,
        "y": 760,
        "wires": [
            [
                "4037d959.803b28",
                "787665f9.79a2bc"
            ]
        ]
    }
]
