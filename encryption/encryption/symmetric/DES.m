function des_encryption()
    clc; clear;

    % Input plaintext and key
    plaintext = input('Enter plaintext (8 characters only): ', 's');
    key = input('Enter key (8 characters only): ', 's');

    % Ensure inputs are exactly 8 characters
    if length(plaintext) ~= 8 || length(key) ~= 8
        error('Plaintext and key must be exactly 8 characters!');
    end

    % Convert plaintext and key to binary
    plaintext_bin = text_to_binary(plaintext);
    key_bin = text_to_binary(key);
    
    % Generate subkeys
    subkeys = generate_subkeys(key_bin);
    
    % Perform encryption
    ciphertext_bin = des_encrypt(plaintext_bin, subkeys);
    
    fprintf('Final Ciphertext: %s\n', ciphertext_bin);
end

% Convert text to binary
function bin_str = text_to_binary(text)
    bin_str = '';
    for i = 1:length(text)
        bin_str = strcat(bin_str, dec2bin(uint8(text(i)), 8)); % Each char -> 8 bits
    end
end

% Perform DES encryption
function ciphertext = des_encrypt(plaintext, subkeys)
    % Initial permutation
    plaintext = permute_bits(plaintext, initial_permutation());

    % Split into L and R
    L = plaintext(1:32);
    R = plaintext(33:64);

    % 16 Rounds of DES
    for i = 1:16
        prev_L = L;
        prev_R = R;

        % Use subkey (First 32 bits)
        round_key = subkeys{i}(1:32);

        % Apply F function
        f_output = f_function(R, round_key); 

        % XOR with previous L
        L = R;
        R = xor_binary(prev_L, f_output);

        % Print round details
        fprintf('Round %d:\n', i);
        fprintf('Key: %s\n', round_key);
        fprintf('L = %s\n', L);
        fprintf('R = %s\n\n', R);
    end

    % Final permutation
    ciphertext = permute_bits([R, L], final_permutation());
end

% Generate subkeys (Dummy implementation)
function subkeys = generate_subkeys(key)
    subkeys = cell(1, 16);
    for i = 1:16
        subkeys{i} = key; % In real DES, subkeys are derived differently
    end
end

% Permutation function
function output = permute_bits(input, table)
    output = input(table);
end

% F function (Basic XOR)
function output = f_function(R, key_part)
    output = xor_binary(R, key_part);
end

% XOR two binary strings
function result = xor_binary(a, b)
    result = char(xor(a - '0', b - '0') + '0');
end

% Initial and Final Permutation Tables (Simplified)
function table = initial_permutation()
    table = [58 50 42 34 26 18 10 2 60 52 44 36 28 20 12 4 ...
             62 54 46 38 30 22 14 6 64 56 48 40 32 24 16 8 ...
             57 49 41 33 25 17 9 1 59 51 43 35 27 19 11 3 ...
             61 53 45 37 29 21 13 5 63 55 47 39 31 23 15 7];
end

function table = final_permutation()
    table = [40 8 48 16 56 24 64 32 39 7 47 15 55 23 63 31 ...
             38 6 46 14 54 22 62 30 37 5 45 13 53 21 61 29 ...
             36 4 44 12 52 20 60 28 35 3 43 11 51 19 59 27 ...
             34 2 42 10 50 18 58 26 33 1 41 9 49 17 57 25];
end
