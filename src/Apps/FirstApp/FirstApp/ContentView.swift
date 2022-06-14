//
//  ContentView.swift
//  FirstApp
//
//  Created by Jonah Makowski on 2022-06-13.
//

import SwiftUI

struct ContentView: View {
    @State private var increment = 0
    @State private var menu = 0
    
    var body: some View {
        if menu == 0 {
            Button("\(increment)") {
                increment += 1
            }
            Button("Reset") {
                increment = 0
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            ContentView()
        }
        .font(.system(size: 40, weight: .bold))
    }
}
