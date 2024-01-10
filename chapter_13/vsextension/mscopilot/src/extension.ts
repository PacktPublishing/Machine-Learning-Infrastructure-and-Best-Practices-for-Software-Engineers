// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import { isDefined } from '@vscode/test-electron/out/util';
import * as vscode from 'vscode';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "mscopilot" is now active!');
	

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommands
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('mscopilot.get_suggestion', async () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user

		let x:string = 'Result: '; 		

		vscode.window.showInformationMessage('Hello World from ms_copilot!');


		const fetch = require('node-fetch');

		const res = await fetch('http://www.google.com');
		const txt = await res.text();

		x += txt;
		
		vscode.window.showInformationMessage(x); 
		
	});

	// Define a command to check which code is selected. 
	vscode.commands.registerCommand('mscopilot.logSelectedText', () => {

		// libraries needed to execute python scripts
		const python = require('python-shell');
		const path = require('path');
	
		// set up the path to the right python interpreter
		// in case we have many, e.g., when using a virtual environment
		python.PythonShell.defaultOptions = { pythonPath: 'C:/Python311/python.exe' };
		// Get the active text editor
		const editor = vscode.window.activeTextEditor;
		
		let selectedText:string = "";

		// Get the selected text
		selectedText = editor!.document.getText(editor!.selection);
		
		// prompt is the same as the selected text
		let prompt:string = selectedText;

		// this is the script in Python that we need to execute in order to 
		// get the code generation
		//
		// please note the strange formatting, 
		// which is necessary as python is very sensitive to indentation
		let scriptText = `
from transformers import pipeline

pipe = pipeline("text-generation", model="codeparrot/codeparrot-small")
outputs = pipe("${prompt}", max_new_tokens=30, do_sample=False)
print(outputs[0]['generated_text'])`;


		// Let the user know what we start the code generation
		vscode.window.showInformationMessage(`Starting code generation for prompt: ${prompt}`);
		
		// run the script and get the message back
		python.PythonShell.runString(scriptText, null).then(messages=>{
			console.log(messages); 

			// get the active editor so that we can paste the code there
			let activeEditor = vscode.window.activeTextEditor;

			
			// paste the generated code snippet
			activeEditor!.edit((selectedText) => {
			
				// when we get the response, we need to format it
				// as one string, not an array of strings
				let snippet = messages.join('\n');

			
				// and replace the selected text with the output
				selectedText.replace(activeEditor!.selection, snippet);
			
				// just logging the content of the snippet
				// to the console
				console.log(snippet);
			
			});
		
		}).then(()=>{
			vscode.window.showInformationMessage(`Code generation finished!`);
		});
	
	});

	context.subscriptions.push(disposable);
}

// This method is called when your extension is deactivated
export function deactivate() {}
